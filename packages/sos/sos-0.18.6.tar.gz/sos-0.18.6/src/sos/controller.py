#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.
import os
import sys
import zmq
import time
import threading
from collections import defaultdict
from .utils import env
from .signatures import StepSignatures, WorkflowSignatures


# from zmq.utils.monitor import recv_monitor_message

def connect_controllers(context=None):
    if not context:
        env.logger.trace(f'create context at {os.getpid()}')
        context = zmq.Context()
    env.logger.trace(f'Connecting sockets from {os.getpid()}')

    env.signature_push_socket = context.socket(zmq.PUSH)
    env.signature_push_socket.connect(
        f'tcp://127.0.0.1:{env.config["sockets"]["signature_push"]}')
    env.signature_req_socket = context.socket(zmq.REQ)
    env.signature_req_socket.connect(
        f'tcp://127.0.0.1:{env.config["sockets"]["signature_req"]}')

    env.controller_push_socket = context.socket(zmq.PUSH)
    env.controller_push_socket.connect(
        f'tcp://127.0.0.1:{env.config["sockets"]["controller_push"]}')
    env.controller_req_socket = context.socket(zmq.REQ)
    env.controller_req_socket.connect(
        f'tcp://127.0.0.1:{env.config["sockets"]["controller_req"]}')

    env.substep_frontend_socket = context.socket(zmq.PUSH)
    env.substep_frontend_socket.connect(
        f'tcp://127.0.0.1:{env.config["sockets"]["substep_frontend"]}')

    # if this instance of sos is being tapped. It should connect to a few sockets
    #
    if env.config['exec_mode'] == 'slave':
        env.tapping_logging_socket = context.socket(zmq.PUSH)
        env.tapping_logging_socket.connect(
            f'tcp://127.0.0.1:{env.config["sockets"]["tapping_logging"]}')
        # change logging to socket
        env.set_socket_logger(env.tapping_logging_socket)

    # master also need to update task status from interactive runner.
    if env.config['exec_mode'] in ('master', 'slave'):
        env.tapping_listener_socket = context.socket(zmq.PUSH)
        env.tapping_listener_socket.connect(
            f'tcp://127.0.0.1:{env.config["sockets"]["tapping_listener"]}')

    return context


def disconnect_controllers(context=None):
    env.signature_push_socket.LINGER = 0
    env.signature_push_socket.close()
    env.signature_req_socket.LINGER = 0
    env.signature_req_socket.close()
    env.controller_push_socket.LINGER = 0
    env.controller_push_socket.close()
    env.controller_req_socket.LINGER = 0
    env.controller_req_socket.close()
    env.substep_frontend_socket.LINGER = 0
    env.substep_frontend_socket.close()

    if env.config['exec_mode'] == 'slave':
        env.tapping_logging_socket.LINGER = 0
        env.tapping_logging_socket.close()
        env.set_socket_logger(None)

    if env.config['exec_mode'] in ('master', 'slave'):
        env.tapping_listener_socket.LINGER = 0
        env.tapping_listener_socket.close()

    env.logger.trace(f'Disconnecting sockets from {os.getpid()}')

    if context:
        env.logger.trace(f'terminate context at {os.getpid()}')
        context.term()

class DotProgressBar:
    def __init__(self, context, interval=1):
        self.context = context
        self.interval = interval * 1000

        self._subprogressbar_size = 25
        self._substep_last_updated = time.time()

        self.stop_event = threading.Event()
        self._substep_cnt = 0

        # broker to handle the execution of substeps
        self.progress_push_socket = self.context.socket(zmq.PUSH)
        self.progress_port = self.progress_push_socket.bind_to_random_port(
            'tcp://127.0.0.1')

        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        progress_pull_socket = self.context.socket(zmq.PULL)
        progress_pull_socket.connect(f'tcp://127.0.0.1:{self.progress_port}')

        # leading progress bar
        sys.stderr.write('\033[32m[\033[0m')
        sys.stderr.flush()

        _pulse_cnt = 0
        while True:
            # no new message, add pulse
            if self.stop_event.is_set():
                return
            if not progress_pull_socket.poll(self.interval):
                if _pulse_cnt == 10:
                    sys.stderr.write('\b \b'*_pulse_cnt)
                    _pulse_cnt = 0
                else:
                    sys.stderr.write('\033[97m.\033[0m')
                    _pulse_cnt += 1
                sys.stderr.flush()
            else:
                msg = progress_pull_socket.recv().decode()
                # print update message
                sys.stderr.write('\b \b'*_pulse_cnt + msg)
                _pulse_cnt = 0
                sys.stderr.flush()

    def update(self, type, status=None):
        if type == 'substep_ignored':
            if time.time() - self._substep_last_updated < 1:
                return
            if self._substep_cnt == self._subprogressbar_size:
                update_str = '\b \b'* self._substep_cnt + '\033[90m.\033[0m'
                self._substep_cnt = 0
            else:
                update_str = '\033[90m.\033[0m'
            self._substep_cnt += 1
            self._substep_last_updated = time.time()
        elif type == 'substep_completed':
            if time.time() - self._substep_last_updated < 1:
                return
            if self._substep_cnt == self._subprogressbar_size:
                update_str = '\b \b'* self._substep_cnt + '\033[32m.\033[0m'
                self._substep_cnt = 0
            else:
                update_str = '\033[32m.\033[0m'
            self._substep_cnt += 1
            self._substep_last_updated = time.time()
        elif type == 'step_completed':
            update_str = '\b \b'*self._substep_cnt
            self._substep_cnt = 0
            if status == 1:  # completed
                update_str += '\033[32m#\033[0m'
            elif status == 0:  # completed
                update_str += '\033[90m#\033[0m'
            elif status > 0:  # in the middle
                update_str += '\033[36m#\033[0m'
            else:  # untracked (no signature)
                update_str += '\033[33m#\033[0m'
        elif type == 'done':
            update_str = '\b \b' * self._substep_cnt + f'\033[32m]\033[0m {status}\n'
            self._substep_cnt = 0

        self.progress_push_socket.send(update_str.encode())

    def done(self, msg):
        self.update('done', msg)
        self.stop_event.set()

class Controller(threading.Thread):
    '''This controller is used by both sos and sos-notebook, and there
    can be two controllers one as a slave (sos) and one as a master
    (notebook). We shared the same code base because step executors need
    need to talk to the same controller (signature, controller etc) when
    they are executed in sos or sos notebook.
    '''
    LRU_READY = b"\x01"

    def __init__(self, ready, kernel=None):
        threading.Thread.__init__(self)
        #self.daemon = True

        self.step_signatures = StepSignatures()
        self.workflow_signatures = WorkflowSignatures()

        self.ready = ready
        self.kernel = kernel
        # number of active running master processes
        self._nprocs = 0

        self._completed = defaultdict(int)
        self._ignored = defaultdict(int)

        # completed steps
        self._completed_steps = {}

        # substgep workers
        self._frontend_requests = []
        self._substep_workers = []
        self._n_working_workers = 0
        self._worker_pending_time = []
        # self.event_map = {}
        # for name in dir(zmq):
        #     if name.startswith('EVENT_'):
        #         value = getattr(zmq, name)
        #          self.event_map[value] = name
        self.console_logger = None

    def handle_sig_push_msg(self, msg):
        try:
            if msg[0] == 'workflow':
                self.workflow_signatures.write(*msg[1:])
            elif msg[0] == 'step':
                self.step_signatures.set(*msg[1:])
            elif msg[0] == 'commit':
                self.workflow_signatures.commit()
                self.step_signatures.commit()
            else:
                env.logger.warning(f'Unknown message passed {msg}')
        except Exception as e:
            env.logger.warning(f'Failed to push signature {msg}: {e}')

    def handle_sig_req_msg(self, msg):
        try:
            # make sure all records have been saved before returning information
            while True:
                if self.sig_push_socket.poll(0):
                    self.handle_sig_push_msg(self.sig_push_socket.recv_pyobj())
                else:
                    break
            if msg[0] == 'workflow':
                if msg[1] == 'clear':
                    self.workflow_signatures.clear()
                    self.sig_req_socket.send_pyobj('ok')
                elif msg[1] == 'placeholders':
                    self.sig_req_socket.send_pyobj(
                        self.workflow_signatures.placeholders(msg[2]))
                elif msg[1] == 'records':
                    self.sig_req_socket.send_pyobj(
                        self.workflow_signatures.records(msg[2]))
                else:
                    env.logger.warning(f'Unknown signature request {msg}')
            elif msg[0] == 'step':
                if msg[1] == 'get':
                    self.sig_req_socket.send_pyobj(
                        self.step_signatures.get(*msg[2:]))
                else:
                    env.logger.warning(f'Unknown signature request {msg}')
            else:
                raise RuntimeError(f'Unrecognized signature request {msg}')
        except Exception as e:
            env.logger.warning(
                f'Failed to respond to signature request {msg}: {e}')
            self.sig_req_socket.send_pyobj(None)

    def handle_ctl_push_msg(self, msg):
        try:
            if msg[0] == 'nprocs':
                env.logger.trace(f'Active running process set to {msg[1]}')
                self._nprocs = msg[1]
            elif msg[0] == 'progress':
                if msg[1] == 'substep_ignored':
                    self._ignored[msg[2]] += 1
                elif msg[1] == 'substep_completed':
                    self._completed[msg[2]] += 1
                elif msg[1] == 'step_completed':
                    self._completed_steps[msg[3]] = msg[4]
                if env.verbosity == 1 and env.config['run_mode'] != 'interactive':
                    # update progress bar
                    self._progress_bar.update(msg[1], msg[2] if len(msg) > 2 else None)
            else:
                raise RuntimeError(f'Unrecognized request {msg}')
        except Exception as e:
            env.logger.warning(f'Failed to push controller {msg}: {e}')

    def handle_ctl_req_msg(self, msg):
        try:
            # handle all sig_push_msg
            while True:
                if self.sig_push_socket.poll(0):
                    self.handle_sig_push_msg(self.sig_push_socket.recv_pyobj())
                else:
                    break
            # also handle ctrl push, which includes progress info
            while True:
                if self.ctl_push_socket.poll(0):
                    self.handle_ctl_push_msg(self.ctl_push_socket.recv_pyobj())
                else:
                    break
            if msg[0] == 'nprocs':
                self.ctl_req_socket.send_pyobj(self._nprocs)
            elif msg[0] == 'sos_step':
                self.ctl_req_socket.send_pyobj(msg[1] in self._completed_steps
                                               or msg[1] in [x.rsplit('_', 1)[0] for x in self._completed_steps.keys()])
            elif msg[0] == 'step_output':
                step_name = msg[1]
                if step_name in self._completed_steps:
                    self.ctl_req_socket.send_pyobj(self._completed_steps[step_name])
                else:
                    # now, step_name might actually be a workflow name, in which
                    # case we need to return the last step of the workflow
                    steps = sorted([x for x in self._completed_steps.keys() if x.rsplit('_', 1)[0] == step_name])
                    self.ctl_req_socket.send_pyobj(self._completed_steps[steps[-1]] if steps else None)
            elif msg[0] == 'named_output':
                name = msg[1]
                found = False
                for step_output in self._completed_steps.values():
                    if name in step_output.labels:
                        found = True
                        self.ctl_req_socket.send_pyobj(step_output[name])
                        break
                if not found:
                    self.ctl_req_socket.send_pyobj(None)
            elif msg[0] == 'done':
                # handle all ctl_push_msgs #1062
                while True:
                    if self.ctl_push_socket.poll(0):
                        self.handle_ctl_push_msg(
                            self.ctl_push_socket.recv_pyobj())
                    else:
                        break

                # handle all push request from substep, used to for example kill workers
                while True:
                    if self.substep_backend_socket.poll(0):
                        self.handle_substep_backend_msg(
                            self.substep_backend_socket.recv())
                    else:
                        break
                # handle all push request from logging
                if env.config['exec_mode'] in ('master', 'both'):
                    while True:
                        if self.tapping_logging_socket.poll(0):
                            self.handle_tapping_logging_msg(
                                self.tapping_logging_socket.recv_multipart())
                        else:
                            break

                if env.verbosity == 1 and env.config['run_mode'] != 'interactive':
                    nSteps = len(set(self._completed.keys())
                                 | set(self._ignored.keys()))
                    nCompleted = sum(self._completed.values())
                    nIgnored = sum(self._ignored.values())
                    completed_text = f'{nCompleted} job{"s" if nCompleted > 1 else ""} completed' if nCompleted else ''
                    ignored_text = f'{nIgnored} job{"s" if nIgnored > 1 else ""} ignored' if nIgnored else ''
                    steps_text = f'{nSteps} step{"s" if nSteps > 1 else ""} processed'
                    succ = '' if msg[1] else 'Failed with '
                    self._progress_bar.done(f'{succ}{steps_text} ({completed_text}{", " if nCompleted and nIgnored else ""}{ignored_text})')

                self.ctl_req_socket.send_pyobj('bye')

                return False
            else:
                raise RuntimeError(f'Unrecognized request {msg}')
            return True
        except Exception as e:
            env.logger.warning(f'Failed to respond controller {msg}: {e}')
            self.ctl_req_socket.send_pyobj(None)

    def handle_substep_frontend_msg(self, msg):

        if self._worker_pending_time:
            self.substep_backend_socket.send(msg)
            self._worker_pending_time.pop()
            return

        #  Get client request, route to first available worker
        self._frontend_requests.insert(0, msg)

        if self._n_working_workers == 0 or self._n_working_workers + self._nprocs < env.config['max_procs']:
            from .workers import SoS_SubStep_Worker
            worker = SoS_SubStep_Worker(env.config)
            worker.start()
            self._substep_workers.append(worker)
            self._n_working_workers += 1
            env.logger.debug(
                f'Start a substep worker, {self._n_working_workers} in total')

    def handle_substep_backend_msg(self, msg):
        # Use worker address for LRU routing
        if not msg:
            return False

        # Forward message to client if it's not a READY
        if msg != self.LRU_READY:
            raise RuntimeError(
                f'substep worker should only send ready message: {msg} received')

        # now see if we have any work to do
        if self._frontend_requests:
            msg = self._frontend_requests.pop()
            self.substep_backend_socket.send(msg)
        else:
            self._worker_pending_time.insert(0, time.time())

    def handle_tapping_logging_msg(self, msg):
        if env.config['exec_mode'] == 'both':
            print(' '.join(x.decode() for x in msg))
        elif msg[0] == b'ERROR':
            env.logger.error(msg[1].decode())
        elif msg[0] == b'WARNING':
            env.logger.warning(msg[1].decode())
        elif msg[0] == b'INFO':
            env.logger.info(msg[1].decode())
        elif msg[0] == b'DEBUG':
            env.logger.debug(msg[1].decode())
        elif msg[0] == b'TRACE':
            env.logger.trace(msg[1].decode())
        elif msg[0] == b'PRINT':
            env.logger.print(*[x.decode() for x in msg[1:]])
        else:
            print(' '.join(x.decode() for x in msg))

    def handle_tapping_listener_msg(self, msg):
        try:
            #env.log_to_file(f'listener got {msg}')
            self.kernel.send_frontend_msg(msg['msg_type'], msg['data'])
        except Exception as e:
            env.log_to_file(
                f'Failed to handle tapping listerner message {msg}: {e}')

    def handle_tapping_controller_msg(self, msg):
        self.tapping_controller_socket.send(b'ok')

    def run(self):
        # there are two sockets
        #
        # signature_push is used to write signatures. It is a single push operation with no reply.
        # signature_req is used to query information. The sender would need to get an response.

        self.context = zmq.Context.instance()

        env.logger.trace(f'controller started {os.getpid()}')

        if 'sockets' not in env.config:
            env.config['sockets'] = {}

        self.sig_push_socket = self.context.socket(zmq.PULL)
        env.config['sockets']['signature_push'] = self.sig_push_socket.bind_to_random_port(
            'tcp://127.0.0.1')
        self.sig_req_socket = self.context.socket(zmq.REP)
        env.config['sockets']['signature_req'] = self.sig_req_socket.bind_to_random_port(
            'tcp://127.0.0.1')

        self.ctl_push_socket = self.context.socket(zmq.PULL)
        env.config['sockets']['controller_push'] = self.ctl_push_socket.bind_to_random_port(
            'tcp://127.0.0.1')
        self.ctl_req_socket = self.context.socket(zmq.REP)
        env.config['sockets']['controller_req'] = self.ctl_req_socket.bind_to_random_port(
            'tcp://127.0.0.1')

        # broker to handle the execution of substeps
        self.substep_frontend_socket = self.context.socket(zmq.PULL)  # ROUTER
        env.config['sockets']['substep_frontend'] = self.substep_frontend_socket.bind_to_random_port(
            'tcp://127.0.0.1')
        self.substep_backend_socket = self.context.socket(zmq.REP)  # ROUTER
        env.config['sockets']['substep_backend'] = self.substep_backend_socket.bind_to_random_port(
            'tcp://127.0.0.1')

        # tapping
        if env.config['exec_mode'] == 'master':
            self.tapping_logging_socket = self.context.socket(zmq.PULL)
            env.config['sockets']['tapping_logging'] = self.tapping_logging_socket.bind_to_random_port(
                'tcp://127.0.0.1')

            self.tapping_listener_socket = self.context.socket(zmq.PULL)
            env.config['sockets']['tapping_listener'] = self.tapping_listener_socket.bind_to_random_port(
                'tcp://127.0.0.1')

            self.tapping_controller_socket = self.context.socket(zmq.PUSH)
            env.config['sockets']['tapping_controller'] = self.tapping_controller_socket.bind_to_random_port(
                'tcp://127.0.0.1')

        if env.config['exec_mode'] == 'slave':
            self.tapping_controller_socket = self.context.socket(zmq.PULL)
            self.tapping_controller_socket.connect(
                f'tcp://127.0.0.1:{env.config["sockets"]["tapping_controller"]}')

        #monitor_socket = self.sig_req_socket.get_monitor_socket()
        # tell others that the sockets are ready
        self.ready.set()

        # Process messages from receiver and controller
        poller = zmq.Poller()
        poller.register(self.sig_push_socket, zmq.POLLIN)
        poller.register(self.sig_req_socket, zmq.POLLIN)
        poller.register(self.ctl_push_socket, zmq.POLLIN)
        poller.register(self.ctl_req_socket, zmq.POLLIN)
        poller.register(self.substep_frontend_socket, zmq.POLLIN)
        poller.register(self.substep_backend_socket, zmq.POLLIN)
        if env.config['exec_mode'] == 'master':
            poller.register(self.tapping_logging_socket, zmq.POLLIN)
            poller.register(self.tapping_listener_socket, zmq.POLLIN)
        if env.config['exec_mode'] == 'slave':
            poller.register(self.tapping_controller_socket, zmq.POLLIN)

        #poller.register(monitor_socket, zmq.POLLIN)
        if env.verbosity == 1 and env.config['run_mode'] != 'interactive':
            # leading progress bar
            self._progress_bar = DotProgressBar(self.context)

        try:
            while True:
                socks = dict(poller.poll())
                if self.sig_push_socket in socks:
                    self.handle_sig_push_msg(self.sig_push_socket.recv_pyobj())

                if self.sig_req_socket in socks:
                    self.handle_sig_req_msg(self.sig_req_socket.recv_pyobj())

                if self.ctl_push_socket in socks:
                    self.handle_ctl_push_msg(self.ctl_push_socket.recv_pyobj())

                if self.ctl_req_socket in socks:
                    if not self.handle_ctl_req_msg(self.ctl_req_socket.recv_pyobj()):
                        break

                if self.substep_frontend_socket in socks:
                    while True:
                        if self.substep_frontend_socket.poll(0):
                            self.handle_substep_frontend_msg(
                                self.substep_frontend_socket.recv())
                        else:
                            break

                if self.substep_backend_socket in socks:
                    while True:
                        if self.substep_backend_socket.poll(0):
                            self.handle_substep_backend_msg(
                                self.substep_backend_socket.recv())
                        else:
                            break

                if env.config['exec_mode'] == 'master':
                    if self.tapping_logging_socket in socks:
                        self.handle_tapping_logging_msg(
                            self.tapping_logging_socket.recv_multipart())
                    if self.tapping_listener_socket in socks:
                        self.handle_tapping_listener_msg(
                            self.tapping_listener_socket.recv_pyobj())

                if env.config['exec_mode'] == 'slave':
                    if self.tapping_controller_socket in socks:
                        self.handle_tapping_controller_msg(
                            self.tapping_controller_socket.recv_pyobj())

                # if the last worker has been pending for more than 5
                # seconds, kill it
                if self._worker_pending_time:
                    now = time.time()
                    kept = [x for x in self._worker_pending_time if now - x < 30]
                    n_kill = len(self._worker_pending_time) - len(kept)
                    if n_kill > 0:
                        for i in range(n_kill):
                            self.substep_backend_socket.send_pyobj(None)
                        self._n_working_workers -= n_kill
                        self._worker_pending_time = [now]*len(kept)
                        env.logger.debug(
                            f'Kill {n_kill} substep worker. {self._n_working_workers} remains.')
                # if monitor_socket in socks:
                #     evt = recv_monitor_message(monitor_socket)
                #     if evt['event'] == zmq.EVENT_ACCEPTED:
                #         self._num_clients += 1
                #     elif evt['event'] == zmq.EVENT_DISCONNECTED:
                #         self._num_clients -= 1
        except Exception as e:
            sys.stderr.write(f'{env.config["exec_mode"]} get an error {e}')
            return
        finally:
            # kill all workers
            for worker in self._worker_pending_time:
                self.substep_backend_socket.send_pyobj(None)

            # close all databses
            self.step_signatures.close()
            self.workflow_signatures.close()

            poller.unregister(self.sig_push_socket)
            poller.unregister(self.sig_req_socket)
            poller.unregister(self.ctl_push_socket)
            poller.unregister(self.ctl_req_socket)
            poller.unregister(self.substep_frontend_socket)
            poller.unregister(self.substep_backend_socket)
            if env.config['exec_mode'] == 'master':
                poller.unregister(self.tapping_logging_socket)
                poller.unregister(self.tapping_listener_socket)
            if env.config['exec_mode'] == 'slave':
                poller.unregister(self.tapping_controller_socket)

            self.sig_push_socket.LINGER = 0
            self.sig_push_socket.close()
            self.sig_req_socket.LINGER = 0
            self.sig_req_socket.close()
            self.ctl_push_socket.LINGER = 0
            self.ctl_push_socket.close()
            self.ctl_req_socket.LINGER = 0
            self.ctl_req_socket.close()
            self.substep_frontend_socket.LINGER = 0
            self.substep_frontend_socket.close()
            self.substep_backend_socket.LINGER = 0
            self.substep_backend_socket.close()
            if env.config['exec_mode'] == 'master':
                self.tapping_logging_socket.LINGER = 0
                self.tapping_logging_socket.close()
                self.tapping_listener_socket.LINGER = 0
                self.tapping_listener_socket.close()
            # both master and slave has it
            if env.config['exec_mode'] in ('master', 'slave'):
                self.tapping_controller_socket.LINGER = 0
                self.tapping_controller_socket.close()

            env.logger.trace(f'controller stopped {os.getpid()}')
