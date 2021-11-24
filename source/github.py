import os


def gh_print(command: str, value: str = "") -> None:
    """ Github command prints"""
    if os.getenv('GITHUB_ACTIONS') is not None:
        print(f'\n::{command}::{value}') # flush=True


def start_github_group(name: str, prefix="", postfix="") -> None:
    """
    Starts a log group in Github Actions Log
    """
    value = (prefix + " " + name + " " + postfix).strip(" ")
    gh_print('group', value)


def end_github_group() -> None:
    """
    Ends a log group in Github Actions Log
    """
    gh_print('endgroup')
