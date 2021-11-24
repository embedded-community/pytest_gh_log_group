"""
Pytest plugin for github action log grouping.
"""
import pytest
from _pytest.reports import TestReport
from .github import start_github_group, end_github_group, gh_print


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item) -> None:
    """
    Start group "TestName TEST"
    """
    start_github_group(item.name, prefix="TEST")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report: TestReport):
    end_github_group()
    #if report.when == 'setup' and report.failed:
    #    gh_print('alert', 'setup failed')

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item) -> None:
    """
    Start group "TestName SETUP"
    """
    start_github_group(item.name, prefix="TEST", postfix="SETUP")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item) -> None:
    """
    Start group "TestName TEARDOWN"
    """
    start_github_group(item.name, prefix="TEST", postfix="TEARDOWN")


'''
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    """
    Start group "PYTEST SESSION START"
    """
    start_github_group("SESSION START")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):  # pylint: disable=unused-argument
    """ Ends a session """
    end_github_group()
'''


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_fixture_setup(request, fixturedef) -> None:
    """
    Start group "FIXTURE FixtureName"
    """
    fixture_type = f'FIXTURE ({fixturedef.scope})'
    fixture_name = request.fixturename
    request_param = request.param
    param_marks = list(filter(lambda m: m.name == 'parametrize',
                              request.node.own_markers))
    if any(param_marks):
        pmark = param_marks[0]
        if pmark is not None and fixture_name in pmark.args[0].split(','):
            # this "fixture" is a pytest parameterize mark
            fixture_type = 'PARAMETER'
            fixture_name = f'{fixture_name} {request_param}'

    start_github_group(prefix=fixture_type,
                       name=fixture_name,
                       postfix=f'SETUP')

    # yield fixture to insert fixture_finalizer at the
    # end of finalizers list (--> executed first)
    yield

    end_github_group()

    def fixture_finalizer():
        """
        Start group for fixture finalization (teardown)
        """
        #start_github_group(prefix=fixture_type,
        #                   name=fixture_name,
        #                   postfix=f'TEARDOWN')

    fixturedef.addfinalizer(fixture_finalizer)
