## pytest github log grouping plugin

This plugin provides grouping functionality for github action console view.

![img.png](img.png)

### Usage

```
pip install pytest_gh_log_group
```

plugin name: `pytest_gh_log_group`

activated by env variable: `GITHUB_ACTIONS`. By default github action have this variable.


### NOTE

because this utilize github console commands there should not be used reporters that doesn't print whole lines, 
like default "dot" reporter. Please use `--no-header -v`  for example
