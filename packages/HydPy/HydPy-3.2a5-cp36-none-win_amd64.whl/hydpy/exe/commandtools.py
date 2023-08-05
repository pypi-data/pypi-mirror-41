# -*- coding: utf-8 -*-
"""This module implements some main features for using *HydPy* from
your command line tools via script |hyd|."""
# import...
# ...from standard library
from typing import IO
import contextlib
import datetime
import inspect
import os
import subprocess
import sys
import time
import traceback
# ...from hydpy
from hydpy import pub
from hydpy.core import autodoctools
from hydpy.core import objecttools


def run_subprocess(commandstring, verbose=True, blocking=True):
    """Execute the given command in a new process.

    Only when both `verbose` and `blocking` are |True|, |run_subprocess|
    prints all responses to the current value of |sys.stdout|:

    >>> from hydpy import run_subprocess
    >>> import platform
    >>> esc = '' if 'windows' in platform.platform().lower() else '\\\\'
    >>> run_subprocess(f'python -c print{esc}(1+1{esc})')
    2

    With verbose being |False|, |run_subprocess| does never print out
    anything:

    >>> run_subprocess(f'python -c print{esc}(1+1{esc})', verbose=False)

    >>> process = run_subprocess('python', blocking=False, verbose=False)
    >>> process.kill()
    >>> _ = process.communicate()

    When `verbose` is |True| and `blocking` is |False|, |run_subprocess|
    prints all responses to the console ("invisible" for doctests):

    >>> process = run_subprocess('python', blocking=False)
    >>> process.kill()
    >>> _ = process.communicate()
    """
    if blocking:
        result = subprocess.run(
            commandstring,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            shell=True)
        if verbose:    # due to doctest replacing sys.stdout
            for output in (result.stdout, result.stderr):
                output = output.strip()
                if output:
                    print(output)
        return None
    else:
        stdouterr = None if verbose else subprocess.DEVNULL
        result = subprocess.Popen(
            commandstring,
            stdout=stdouterr,
            stderr=stdouterr,
            encoding='utf-8',
            shell=True)
        return result


def exec_commands(commands, **parameters) -> None:
    """Execute the given Python commands.

    Function |exec_commands| is thought for testing purposes only (see
    the main documentation on module |hyd|).  Seperate individual commands
    by semicolons and replaced whitespaces with underscores:

    >>> from hydpy.exe.commandtools import exec_commands
    >>> import sys
    >>> exec_commands("x_=_1+1;print(x)")
    Start to execute the commands ['x_=_1+1', 'print(x)'] for testing purposes.
    2

    |exec_commands| interprets double underscores as a single underscores:

    >>> exec_commands("x_=_1;print(x.____class____)")
    Start to execute the commands ['x_=_1', 'print(x.____class____)'] \
for testing purposes.
    <class 'int'>

    |exec_commands| evaluates additional keyword arguments before it
    executes the given commands:

    >>> exec_commands("e=x==y;print(e)", x=1, y=2)
    Start to execute the commands ['e=x==y', 'print(e)'] for testing purposes.
    False
    """
    cmdlist = commands.split(';')
    print(f'Start to execute the commands {cmdlist} for testing purposes.')
    for par, value in parameters.items():
        exec(f'{par} = {value}')
    for command in cmdlist:
        command = command.replace('__', 'temptemptemp')
        command = command.replace('_', ' ')
        command = command.replace('temptemptemp', '_')
        exec(command)


pub.scriptfunctions['exec_commands'] = exec_commands


def print_latest_logfile(dirpath='.', wait=0.0) -> None:
    """Print the latest log file in the current or the given working directory.

    When executing processes in parallel, |print_latest_logfile| may
    be called before any log file exists.  Then pass an appropriate
    number of seconds to the argument `wait`.  |print_latest_logfile| then
    prints the contents of the latest log file, as soon as it finds one.

    See the main documentation on module |hyd| for more information.
    """
    now = time.perf_counter()
    wait += now
    filenames = []
    while now <= wait:
        for filename in os.listdir(dirpath):
            if filename.startswith('hydpy_') and filename.endswith('.log'):
                filenames.append(filename)
        if filenames:
            break
        else:
            time.sleep(0.1)
            now = time.perf_counter()
    if not filenames:
        raise FileNotFoundError(
            f'Cannot find a HydPy log file in directory '
            f'{os.path.abspath(dirpath)}.')
    with open(sorted(filenames)[-1]) as logfile:
        print(logfile.read())


def prepare_logfile(filename=None):
    """Prepare an empty log file eventually and return its absolute path.

    When passing the "filename" `stdout`, |prepare_logfile| does not
    prepare any file and just returns `stdout`:

    >>> from hydpy.exe.commandtools import prepare_logfile
    >>> prepare_logfile('stdout')
    'stdout'

    When passing the "filename" `default`, |prepare_logfile| generates a
    filename containing the actual date and time, prepares an empty file
    on disk, and returns its path:

    >>> from hydpy import repr_, TestIO
    >>> from hydpy.core.testtools import mock_datetime_now
    >>> from datetime import datetime
    >>> with TestIO():
    ...     with mock_datetime_now(datetime(2000, 1, 1, 12, 30, 0)):
    ...         filepath = prepare_logfile('default')
    >>> import os
    >>> os.path.exists(filepath)
    True
    >>> repr_(filepath)    # doctest: +ELLIPSIS
    '...hydpy/tests/iotesting/hydpy_2000-01-01_12-30-00.log'

    For all other strings, |prepare_logfile| does not add any date or time
    information to the filename:

    >>> with TestIO():
    ...     with mock_datetime_now(datetime(2000, 1, 1, 12, 30, 0)):
    ...         filepath = prepare_logfile('my_log_file.txt')
    >>> os.path.exists(filepath)
    True
    >>> repr_(filepath)    # doctest: +ELLIPSIS
    '...hydpy/tests/iotesting/my_log_file.txt'
    """
    if filename == 'stdout':
        return filename
    if filename == 'default':
        filename = datetime.datetime.now().strftime(
            'hydpy_%Y-%m-%d_%H-%M-%S.log')
    with open(filename, 'w'):
        pass
    return os.path.abspath(filename)


@contextlib.contextmanager
def _activate_logfile(filepath, logstyle, level_stdout, level_stderr):
    try:
        if filepath == 'stdout':
            sys.stdout = LogFileInterface(sys.stdout, logstyle, level_stdout)
            sys.stderr = LogFileInterface(sys.stderr, logstyle, level_stderr)
            yield
        else:
            with open(filepath, 'a') as logfile:
                sys.stdout = LogFileInterface(logfile, logstyle, level_stdout)
                sys.stderr = LogFileInterface(logfile, logstyle, level_stderr)
                yield
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__


def execute_scriptfunction():
    """Execute a HydPy script function.

    Function |execute_scriptfunction| is indirectly applied and
    explained in the documentation on module |hyd|.
    """
    try:
        args_given = []
        kwargs_given = {}
        for arg in sys.argv[1:]:
            if len(arg) < 3:
                args_given.append(arg)
            else:
                try:
                    key, value = parse_argument(arg)
                    kwargs_given[key] = value
                except ValueError:
                    args_given.append(arg)
        logfilepath = prepare_logfile(kwargs_given.pop('logfile', 'stdout'))
        logstyle = kwargs_given.pop('logstyle', 'plain')
        try:
            funcname = str(args_given.pop(0))
        except IndexError:
            raise ValueError(
                'The first positional argument defining the function '
                'to be called is missing.')
        try:
            func = pub.scriptfunctions[funcname]
        except KeyError:
            available_funcs = objecttools.enumeration(
                sorted(pub.scriptfunctions.keys()))
            raise ValueError(
                f'There is no `{funcname}` function callable by `hyd.py`.  '
                f'Choose one of the following instead: {available_funcs}.')
        args_required = inspect.getfullargspec(func).args
        nmb_args_required = len(args_required)
        nmb_args_given = len(args_given)
        if nmb_args_given != nmb_args_required:
            enum_args_given = ''
            if nmb_args_given:
                enum_args_given = (
                    f' ({objecttools.enumeration(args_given)})')
            enum_args_required = ''
            if nmb_args_required:
                enum_args_required = (
                    f' ({objecttools.enumeration(args_required)})')
            raise ValueError(
                f'Function `{funcname}` requires `{nmb_args_required:d}` '
                f'positional arguments{enum_args_required}, but '
                f'`{nmb_args_given:d}` are given{enum_args_given}.')
        with _activate_logfile(logfilepath, logstyle, 'info', 'warning'):
            func(*args_given, **kwargs_given)
    except BaseException as exc:
        if logstyle not in LogFileInterface.style2infotype2string:
            logstyle = 'plain'
        with _activate_logfile(logfilepath, logstyle, 'exception', 'exception'):
            arguments = ', '.join(sys.argv)
            print(f'Invoking hyd.py with arguments `{arguments}` '
                  f'resulted in the following error:\n{str(exc)}\n\n'
                  f'See the following stack traceback for debugging:\n',
                  file=sys.stderr)
            traceback.print_tb(sys.exc_info()[2])


class LogFileInterface(object):
    """Wraps a usual file object, exposing all its methods while modifying
    only the `write` method.

    At the moment, class |LogFileInterface| only supports only two log
    styles, as explained in the documentation on module |hyd|.  The
    following example shows its basic usage:

    >>> from hydpy import TestIO
    >>> from hydpy.exe.commandtools import LogFileInterface
    >>> with TestIO():
    ...     logfile = open('test.log', 'w')
    >>> lfi = LogFileInterface(
    ...     logfile, logstyle='prefixed', infotype='exception')
    >>> lfi.write('a message\\n')
    >>> lfi.write('another message\\n')
    >>> lfi.close()
    >>> with TestIO():
    ...     with open('test.log', 'r') as logfile:
    ...         print(logfile.read())
    error: a message
    error: another message
    <BLANKLINE>

    The class member `style2infotype2string` defines the currently
    available log styles.
    """

    style2infotype2string = {
        'plain': {'info': '',
                  'warning': '',
                  'exception': ''},
        'prefixed': {'info': 'info: ',
                     'warning': 'warning: ',
                     'exception': 'error: '}}

    def __init__(self, logfile: IO, logstyle: str, infotype: str):
        self.logfile = logfile
        try:
            stdtype2string = self.style2infotype2string[logstyle]
        except KeyError:
            styles = objecttools.enumeration(
                sorted(self.style2infotype2string.keys()))
            raise ValueError(
                f'The given log file style {logstyle} is not available.  '
                f'Please choose one of the following: {styles}.')
        self._string = stdtype2string[infotype]

    def write(self, string):
        self.logfile.write('\n'.join(
            f'{self._string}{substring}' if substring else ''
            for substring in string.split('\n')))

    def __getattr__(self, name):
        return getattr(self.logfile, name)


def parse_argument(string):
    """Return a single value for a string understood as a positional
    argument or a |tuple| containing a keyword and its value for a
    string understood as a keyword argument.

    |parse_argument| is intended to be used as a helper function for
    function |execute_scriptfunction| only.  See the following
    examples to see which types of keyword arguments |execute_scriptfunction|
    covers:

    >>> from hydpy.exe.commandtools import parse_argument
    >>> parse_argument('x=3')
    ('x', '3')
    >>> parse_argument('"x=3"')
    '"x=3"'
    >>> parse_argument("'x=3'")
    "'x=3'"
    >>> parse_argument('x="3==3"')
    ('x', '"3==3"')
    >>> parse_argument("x='3==3'")
    ('x', "'3==3'")
    """
    idx_equal = string.find('=')
    if idx_equal == -1:
        return string
    idx_quote = idx_equal+1
    for quote in ('"', "'"):
        idx = string.find(quote)
        if -1 < idx < idx_quote:
            idx_quote = idx
    if idx_equal < idx_quote:
        return string[:idx_equal], string[idx_equal+1:]
    return string


autodoctools.autodoc_module()
