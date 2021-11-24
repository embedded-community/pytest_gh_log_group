import os
import pytest


def gh_print(key: str, value: str):
    if os.getenv('GITHUB_ACTIONS') is not None:
        print(f'\n::{key}::{value}', flush=True)


def start_github_group(name: str, prefix="", postfix="") -> None:
    """
     Starts a log group in Github Actions Log
     """
    gh_print('group', (prefix + " " + name + " " + postfix).strip(" "))


def end_github_group(name="", prefix="", postfix="") -> None:
    """
    Ends a log group in Github Actions Log
    """
    gh_print('endgroup', (prefix + " " + name + " " + postfix).strip(" "))


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    end_github_group()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item) -> None:
    """
    Start group "TestName TEST"
    """
    start_github_group(item.name, postfix="TEST")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item) -> None:
    """
    Start group "TestName SETUP"
    """
    start_github_group(item.name, postfix="SETUP")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item) -> None:
    """
    Start group "TestName TEARDOWN"
    """
    start_github_group(item.name, postfix="TEARDOWN")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    """
    Start group "PYTEST SESSION START"
    """
    start_github_group("PYTEST SESSION START")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_fixture_setup(request, fixturedef) -> None:
    """
    Start group "FIXTURE FixtureName"
    """
    fixture_type = 'FIXTURE'
    fixture_name = request.fixturename
    request_param = request.param
    param_marks = list(filter(lambda m: m.name == 'parametrize', request.node.own_markers))
    if any(param_marks):
        pmark = param_marks[0]
        if pmark is not None and fixture_name in pmark.args[0].split(','):
            # this "fixture" is a pytest parameterize mark
            fixture_type = f'PARAMETER'
            fixture_name = f'{fixture_name} {request_param}'

    start_github_group(prefix=fixture_type, name=fixture_name, postfix=f'({fixturedef.scope}) SETUP')

    yield  # yield fixture to insert fixture_finalizer at the end of finalizers list (--> executed first)

    def fixture_finalizer():
        """
        Start group for fixture finalization (teardown)
        """
        start_github_group(prefix=fixture_type, name=fixture_name, postfix=f'({fixturedef.scope}) TEARDOWN')

    fixturedef.addfinalizer(fixture_finalizer)
