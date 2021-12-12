""" Github log commands """
import os

# GitHub doesn't support nested grouping so this ensures we do not have any.
GROUP_ACTIVATED = False


def gh_print(command: str, value: str = "") -> None:
    """ Github command prints"""
    if os.getenv('GITHUB_ACTIONS') is not None:
        print(f'::{command}::{value}', flush=True)


def start_github_group(name: str, prefix="", postfix="") -> None:
    """
    Starts a log group in Github Actions Log
    """
    global GROUP_ACTIVATED  # pylint: disable=global-statement

    if GROUP_ACTIVATED:
        # GitHub doesn't support nested grouping
        return

    value = (prefix + " " + name + " " + postfix).strip(" ")
    gh_print('group', value)
    GROUP_ACTIVATED = True


def end_github_group() -> None:
    """
    Ends a log group in Github Actions Log
    """
    global GROUP_ACTIVATED  # pylint: disable=global-statement

    if not GROUP_ACTIVATED:
        # GitHub doesn't support nested grouping
        return
    gh_print('endgroup')
    GROUP_ACTIVATED = False
