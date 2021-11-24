import pytest


@pytest.fixture(scope='session', params=[""])
def session_setup():
    print('session_setup')


@pytest.fixture(scope='function', params=[""])
def test_setup():
    print('test_setup')


def test_sample1(session_setup, test_setup):
    # subprocess.check_call('pytest test_e2e.py', env={'GITHUB_ACTIONS': '1'})
    print('test')


def test_sample2(session_setup, test_setup):
    # subprocess.check_call('pytest test_e2e.py', env={'GITHUB_ACTIONS': '1'})
    print('test')
