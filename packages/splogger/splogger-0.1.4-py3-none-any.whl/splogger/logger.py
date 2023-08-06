from __future__ import print_function
import sys
from colorama import Fore, Style
from datetime import datetime
import threading
from threading import Lock
from threading import Thread
from multiprocessing import Value
import itertools
from time import sleep
from time import time
import atexit
from wrapt import decorator

CROSS = "✘"
TICK = "✓"
SPINNERS = [
    ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁'],
    ['▉', '▊', '▋', '▌', '▍', '▎', '▏', '▎', '▍', '▌', '▋', '▊'],
    ['┤', '┘', '┴', '└', '├', '┌', '┬', '┐'],
    ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
]

CLEAR_LINE = '\033[K'
CR_CL      = '\r'+CLEAR_LINE

INFO  = f'{CR_CL}{Fore.LIGHTGREEN_EX}[{TICK}] {Fore.RESET}'
WARN  = f'{CR_CL}{Fore.YELLOW}[!] {Fore.RESET}'
ERR   = f'{CR_CL}{Fore.RED}[{CROSS}] {Fore.RESET}'
DEBUG = f'{CR_CL}{Fore.LIGHTBLUE_EX}[i] {Fore.RESET}'
FINE  = f'{CR_CL}    {Fore.RESET}'


def DATE(): return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


VERBOSE = False
CURRENT_SPINNER = 3

log_fd = None

originalStdOut = sys.stdout
originalStdErr = sys.stderr


class ProgressActionDisplayer(object):
    def __init__(self):
        self.actions = {}
        self.lock = Lock()
        self.running = Value('i', 0)
        self.comp_info = ''
        atexit.register(self.exit)
        Thread(target=self._action_display_target, daemon=True).start()

    def exit(self):
        # self.lock.acquire()
        if self.running.value:
            originalStdOut.write('\r\033[K\n')

    def start_action(self, action):
        thread_name = threading.current_thread().name
        self.lock.acquire()
        if thread_name not in self.actions:
            self.actions[thread_name] = []
        self.actions[thread_name].append(action)
        self.comp_info = ''
        self.lock.release()

    def finish_action(self):
        thread_name = threading.current_thread().name
        self.lock.acquire()
        self.actions[thread_name].pop()
        self.comp_info = ''
        self.lock.release()

    # Change the current displayed text near spinner to include additional info
    def set_additional_info(self, info):
        self.lock.acquire()
        try:
            if info is None:
                self.comp_info = ''
            if type(info) != str:
                return
            self.comp_info = '('+info+')'
        finally:
            self.lock.release()


    def _action_display_target(self):
        thread_index = 0
        last_thread_index_change = 0
        thread_switch_interval = 1  # in sec


        # def print_at(row, column):
        #     return f'\033[{row};{column}H'

        def make_spinner():
            spinner_chars = SPINNERS[CURRENT_SPINNER]
            return itertools.cycle(spinner_chars)

        def get_action():
            nonlocal thread_index
            self.lock.acquire()
            try:
                keys = self.actions.keys()

                if len(keys) == 0:
                    return None

                if thread_index >= len(keys):
                    thread_index = 0

                thread_name = list(keys)[thread_index]
                action_length = len(self.actions[thread_name])

                if action_length == 0:
                    return None

                # print stack top
                action = self.actions[thread_name][action_length - 1]
            finally:
                self.lock.release()

            return action

        spinner = make_spinner()
        while True:
            sleep(0.1)
            # rows, _ = os.popen('stty size', 'r').read().split()

            if last_thread_index_change + thread_switch_interval > time():
                thread_index += 1
                last_thread_index_change = time()

            action = get_action()
            if not action:
                self.running.value = 0
                continue
            if self.running.value == 0:
                spinner = make_spinner()

            self.running.value = 1

            print(
                f'\r\033[K{Fore.CYAN}{next(spinner)}{Fore.MAGENTA} {action} {self.comp_info}{Fore.RESET}',
                file=originalStdOut,
                end=' ')  # TODO depth
            # {print_at(int(rows), 5)}


class FakeStdObject(object):
    def __init__(self, std_object, print_with):
        self.std_object = std_object
        self.print_with = print_with

    def write(self, obj):
        if obj == '\n':
            return

        if not obj.endswith('\n'):
            obj += '\n'

        self.print_with(obj, self.std_object, '')
        self.flush()

    def flush(self):
        self.std_object.flush()

class LogStdObject(FakeStdObject):
    def __init__(self, originalStd):
        self.std = originalStd

    def write(self, obj):
        global log_fd

        if obj == '\n':
            return

        if not obj.endswith('\n'):
            obj += '\n'

        self.std.write(obj)
        if log_fd != None:
            log_fd.write(obj)
            log_fd.flush()

    def flush(self):
        global log_fd

        if log_fd != None:
            log_fd.flush()
        self.std.flush()

log_stdout = LogStdObject(originalStdOut)
log_stderr = LogStdObject(originalStdErr)

displayer = ProgressActionDisplayer()


def set_verbose(verbose):
    global VERBOSE
    VERBOSE = verbose


def get_verbose():
    global VERBOSE
    return VERBOSE


def fine(msg, file=log_stdout, strong=False, end='\n'):
    print(f'{FINE}{DATE()} : {Style.BRIGHT + Fore.WHITE if strong else ""}{msg}{Fore.RESET + Style.NORMAL}', file=file, end=end)


def success(msg, file=log_stdout, strong=False, end='\n'):
    print(f'{INFO}{DATE()} : {Style.BRIGHT + Fore.LIGHTGREEN_EX if strong else ""}{msg}{Fore.RESET + Style.NORMAL}', file=file, end=end)


def warning(msg, file=log_stdout, strong=False, end='\n'):
    print(f'{WARN}{DATE()} : {Style.BRIGHT + Fore.YELLOW if strong else ""}{msg}{Fore.RESET + Style.NORMAL}', file=file, end=end)


def error(msg, file=log_stderr, strong=False, end='\n'):
    print(f'{ERR}{DATE()} : {Style.BRIGHT + Fore.RED if strong else ""}{msg}{Fore.RESET + Style.NORMAL}', file=file, end=end)


def debug(msg, file=log_stdout, strong=False, end='\n'):
    global VERBOSE
    if VERBOSE:
        print(f'{DEBUG}{DATE()} : {Style.BRIGHT + Fore.LIGHTBLUE_EX if strong else ""}{msg}{Fore.RESET + Style.NORMAL}', file=file, end=end)


std_captured = False


def capture_std_outputs(value=True):
    debug('Switching stdout/err capture to: '+str(value))
    global std_captured
    if std_captured and not value:
        sys.stdout = originalStdOut
        sys.stderr = originalStdErr
        std_captured = False
        return

    if not std_captured and value:
        sys.stdout = FakeStdObject(originalStdOut, fine)
        sys.stderr = FakeStdObject(originalStdErr, error)
        std_captured = True
        return

# decorators


def no_spinner():
    @decorator
    def wrapper(func, instance, args, kwargs):  # FIXME change to ()
        try:
            displayer.start_action(None)
            return func(*args, **kwargs)
        except BaseException as e:
            raise e
        finally:
            displayer.finish_action()
    return wrapper


def unformat():
    @decorator
    def wrapper(func, instance, args, kwargs):
        global std_captured
        v = std_captured
        try:
            if v:
                capture_std_outputs(False)
            return func(*args, **kwargs)
        except BaseException as ex:
            raise ex
        finally:
            capture_std_outputs(v)
    return wrapper


# The console wrapper, show the current action while
# the function is executed
def element(action="", log_entry=False, print_exception=False):
    @decorator
    def wrapper(func, instance, args, kwargs):
        try:
            if log_entry:
                success(f'Starting: {action}')  # TODO depth (by thread)
            displayer.start_action(action)
            result = func(*args, **kwargs)
            if log_entry:
                success(f'Completed: {action}')
        except BaseException as ex:
            # displayer.lock.acquire()
            error(f'Failed: {action}: {ex.__class__.__name__}')
            # if print_exception:
            #     error("TODO : print stack") # TODO
            # displayer.lock.release()
            raise ex
        finally:
            displayer.finish_action()

        return result
    return wrapper

set_additional_info = displayer.set_additional_info

def clear():
    @decorator
    @unformat()
    @no_spinner()
    def wrapper(func, instance, args, kwargs):
        return func(*args, **kwargs)
    return wrapper


def fancy_output(action="", log_entry=False, print_exception=False):
    @decorator
    @element(action, log_entry, print_exception)
    def wrapper(func, instance, args, kwargs):
        return func(*args, **kwargs)
    return wrapper


def auto(log_entry=True, print_exception=True):
    @decorator
    def wrapper(func, instance, args, kwargs):
        @element(func.__name__, log_entry, print_exception)
        def wrapper2(func, instance, args, kwargs):
            return func(*args, **kwargs)
        return wrapper2(func, instance, args, kwargs)
    return wrapper


def use_spinner(index):
    global SPINNERS
    global CURRENT_SPINNER
    assert index >= 0 and index < len(SPINNERS)
    CURRENT_SPINNER = index

def set_log_file(file):
    global log_fd
    if log_fd != None:
        log_fd.close()
        log_fd = None

    if file == None:
        return
    if type(file) == str:
        file = open(file, 'w+')

    log_fd = file


__all__ = [
    "auto",
    "clear",
    "use_spinner",
    "element",
    "no_spinner",
    "capture_std_outputs",
    "success",
    "error",
    "debug",
    "warning",
    "get_verbose",
    "set_verbose",
    "fine",
    "unformat",
    "set_additional_info",
    "set_log_file"]
