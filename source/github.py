""" Github log commands """
import pytest
from _pytest.terminal import TerminalReporter


class Github:
    def __init__(self, reporter: TerminalReporter):
        self._reporter = reporter
        # GitHub doesn't support nested grouping so this ensures we do not have any.
        self._group_activated = False

    def gh_print(self, command: str, value: str = "") -> None:
        """ Github command prints"""
        if self._reporter:
            self._reporter.write_line(f'::{command}::{value}', flush=True)

    def start_github_group(self, name: str, prefix="", postfix="") -> None:
        """
        Starts a log group in Github Actions Log
        """
        if self._group_activated:
            # GitHub doesn't support nested grouping
            return

        value = (prefix + " " + name + " " + postfix).strip(" ")
        self.gh_print('group', value)
        self._group_activated = True

    def end_github_group(self) -> None:
        """
        Ends a log group in Github Actions Log
        """
        if not self._group_activated:
            # GitHub doesn't support nested grouping
            return
        self.gh_print('endgroup')
        self._group_activated = False
