# -*- coding: utf-8 -*-
"""Test all "conventional" unit tests defined in subpackage `tests` and
all doctests defined in the different modules and documentation files.
"""

import os
import sys
import importlib
import unittest
import doctest
import warnings
import matplotlib


class FilterFilenames(object):

    def __init__(self, argv):
        self.selection = []
        for arg_ in argv:
            if arg_.startswith('select='):
                self.selection.extend(_ for _ in arg_[7:].split(','))

    def __call__(self, names) -> list:
        if self.selection:
            return [_ for _ in names if (_ in self.selection)]
        return list(names)


filter_filenames = FilterFilenames(sys.argv)
testpath = None
for arg in sys.argv:
    if arg.startswith('test_path='):
        testpath = arg.split('=')[-1]

forcecompiling = 'forcecompiling=False' not in sys.argv


exitcode = int(os.system('python test_pyplot_backend.py'))
standard_backend_missing = exitcode in (1, 256)
if standard_backend_missing:
    matplotlib.use('Agg')
    print('The standard backend of matplotlib does not seem to be available '
          'on the current system.  Possibly, because you are working on a web '
          'server.  Instead, the widely available backend `Agg` is selected.')

# Priorise site-packages (on Debian-based Linux distributions as Ubuntu
# also dist-packages) in the import order to make sure, the following
# imports refer to the newly build hydpy package on the respective computer.
if testpath is None:
    paths = [path for path in sys.path if path.endswith('-packages')]
    for path in paths:
        sys.path.insert(0, path)
else:
    sys.path.insert(0, testpath)

# Import all hydrological models to trigger the automatic cythonization
# mechanism of HydPy.
from hydpy import pub
pub.options.forcecompiling = forcecompiling
pub.options.skipdoctests = True
import hydpy.models
for name in [fn.split('.')[0] for fn in os.listdir(hydpy.models.__path__[0])]:
    if name != '__init__':
        importlib.import_module('hydpy.models.'+name)
pub.options.skipdoctests = False
pub.options.forcecompiling = False

# Write the required configuration files to be generated dynamically.
from hydpy.auxs.xmltools import XSDWriter
XSDWriter().write_xsd()

# 1. Perform all "classical" unit tests.

import hydpy.tests
filenames = filter_filenames(os.listdir(hydpy.tests.__path__[0]))
unittests = {fn.split('.')[0]: None for fn in filenames if
             (fn.startswith('unittest') and fn.endswith('.py'))}
for name in unittests.keys():
    module = importlib.import_module('hydpy.tests.' + name)
    suite = unittest.TestLoader().loadTestsFromModule(module)
    with open(os.devnull, 'w') as file_:
        runner = unittest.TextTestRunner(stream=file_)
        unittests[name] = runner.run(suite)
    unittests[name].nmbproblems = (len(unittests[name].errors) +
                                   len(unittests[name].failures))

successfulunittests = {name: runner for name, runner in unittests.items()
                       if not runner.nmbproblems}
failedunittests = {name: runner for name, runner in unittests.items()
                   if runner.nmbproblems}

if successfulunittests:
    print()
    print('In the following modules, no unit test failed:')
    for name in sorted(successfulunittests.keys()):
        print('    %s (%d successes)'
              % (name, successfulunittests[name].testsRun))
if failedunittests:
    print()
    print('At least one unit test failed in each of the following modules:')
    for name in sorted(failedunittests.keys()):
        print('    %s (%d failures/errors)'
              % (name, failedunittests[name].nmbproblems))
    for name in sorted(failedunittests.keys()):
        print()
        print('Detailed information on module %s:' % name)
        for idx, problem in enumerate(failedunittests[name].errors +
                                      failedunittests[name].failures):
            print('    Problem no. %d:' % (idx+1))
            print('        %s' % problem[0])
            for line in problem[1].split('\n'):
                print('        %s' % line)

# 2. Perform all doctests (first in Python mode, then in Cython mode)

from hydpy import pub
pub.options.reprcomments = False
import hydpy
from hydpy.core import devicetools
from hydpy.core import parametertools
from hydpy.core import testtools
alldoctests = ({}, {})
allsuccessfuldoctests = ({}, {})
allfaileddoctests = ({}, {})
iterable = zip(('Python', 'Cython'), alldoctests,
               allsuccessfuldoctests, allfaileddoctests)
for (mode, doctests, successfuldoctests, faileddoctests) in iterable:
    pub.options.usecython = mode == 'Cython'
    for dirpath, dirnames, filenames_ in os.walk(hydpy.__path__[0]):
        if (('__init__.py' not in filenames_) or
                dirpath.endswith('tests') or
                dirpath.endswith('__pycache__') or
                dirpath.endswith('build')):
            continue
        filenames_ = filter_filenames(filenames_)
        packagename = dirpath.replace(os.sep, '.')+'.'
        packagename = packagename[packagename.find('hydpy.'):]
        level = packagename.count('.')-1
        modulenames = [packagename+fn.split('.')[0]
                       for fn in filenames_ if fn.endswith('.py')]
        docfilenames = [os.path.join(dirpath, fn)
                        for fn in filenames_ if fn.endswith('.rst')]
        for name in (modulenames + docfilenames):
            if name.split('.')[-1] in ('apidoc', 'prepare', 'modify_html'):
                continue
            if not name.endswith('.rst'):
                module = importlib.import_module(name)
                testtools.solve_exception_doctest_issue(module)
            suite = unittest.TestSuite()
            try:
                if name.endswith('.rst'):
                    suite.addTest(
                        doctest.DocFileSuite(name, module_relative=False,
                                             optionflags=doctest.ELLIPSIS))
                else:
                    suite.addTest(
                        doctest.DocTestSuite(module,
                                             optionflags=doctest.ELLIPSIS))
            except ValueError as exc:
                if exc.args[-1] != 'has no docstrings':
                    raise exc
            else:
                opt = pub.options
                Par = parametertools.Parameter
                with opt.usedefaultvalues(False), \
                        opt.usedefaultvalues(False), \
                        opt.printprogress(False), \
                        opt.printincolor(False), \
                        opt.warnsimulationstep(False), \
                        opt.reprcomments(False), \
                        opt.ellipsis(0), \
                        opt.reprdigits(6), \
                        opt.warntrim(False), \
                        Par.parameterstep.delete(), \
                        Par.simulationstep.delete():
                    del pub.projectname
                    del pub.timegrids
                    devicetools.Node.clear_registry()
                    devicetools.Element.clear_registry()
                    testtools.IntegrationTest.plotting_options = \
                        testtools.PlottingOptions()
                    if name.endswith('.rst'):
                        name = name[name.find('hydpy'+os.sep):]
                    with warnings.catch_warnings(), \
                            open(os.devnull, 'w') as file_:
                        warnings.filterwarnings(
                            'error', module='hydpy')
                        warnings.filterwarnings(
                            'error', category=UserWarning)
                        warnings.filterwarnings(
                            'ignore', category=ImportWarning)
                        warnings.filterwarnings(
                            'ignore', message="numpy.dtype size changed")
                        warnings.filterwarnings(
                            'ignore', message="numpy.ufunc size changed")
                        warnings.filterwarnings(
                            'ignore',
                            message='the imp module is deprecated')
                        runner = unittest.TextTestRunner(stream=file_)
                        doctests[name] = runner.run(suite)
                    doctests[name].nmbproblems = (
                            len(doctests[name].errors) +
                            len(doctests[name].failures))
                    hydpy.dummies.clear()
    successfuldoctests.update({name: runner for (name, runner)
                              in doctests.items() if not runner.nmbproblems})
    faileddoctests.update({name: runner for (name, runner)
                          in doctests.items() if runner.nmbproblems})

    if successfuldoctests:
        print()
        print('In the following modules, no doc test failed in %s mode:'
              % mode)
        for name in sorted(successfuldoctests.keys()):
            if name.endswith('.rst'):
                print('    %s' % name)
            else:
                print('    %s (%d successes)'
                      % (name, successfuldoctests[name].testsRun))
    if faileddoctests:
        print()
        print('At least one doc test failed in each of the following modules '
              'in %s mode:' % mode)
        for name in sorted(faileddoctests.keys()):
            print('    %s (%d failures/errors)'
                  % (name, faileddoctests[name].nmbproblems))
        for name in sorted(faileddoctests.keys()):
            print()
            print('Detailed information on module %s:' % name)
            for idx, problem in enumerate(faileddoctests[name].errors +
                                          faileddoctests[name].failures):
                print('    Error no. %d:' % (idx+1))
                print('        %s' % problem[0])
                for line in problem[1].split('\n'):
                    print('        %s' % line)

# 3. Perform integration tests.


# 4. Return the exit code.
print('\ntest_everything.py resulted in %d failing unit test suites, '
      '%d failing doctest suites in Python mode and %d failing '
      'doctest suites in Cython mode.' % (len(failedunittests),
                                          len(allfaileddoctests[0]),
                                          len(allfaileddoctests[1])))
if failedunittests or allfaileddoctests[0] or allfaileddoctests[1]:
    sys.exit(1)
else:
    sys.exit(0)
