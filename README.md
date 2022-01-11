[![ci](https://github.com/embedded-community/pytest_gh_log_group/actions/workflows/push.yml/badge.svg)](https://github.com/embedded-community/pytest_gh_log_group/actions/workflows/push.yml)
[![PyPI version](https://badge.fury.io/py/pytest-gh-log-group.svg)](https://pypi.org/project/pytest-gh-log-group/)


## pytest github log grouping plugin

This plugin provides grouping functionality for GitHub action console view.

![img.png](img.png)

### Usage

```
pip install pytest_gh_log_group
```

plugin name: `pytest_gh_log_group`

activated by env variable: `GITHUB_ACTIONS`. By default, GitHub action have this variable.


### NOTE

GitHub does not currently support nested groups, see https://github.com/actions/runner/issues/802.
