#
#   Apache License 2.0
#
#   Copyright (c) 2024, Mattias Aabmets
#
#   The contents of this file are subject to the terms and conditions defined in the License.
#   You may not use, modify, or distribute this file except in compliance with the License.
#
#   SPDX-License-Identifier: Apache-2.0
#

import typing as t

from rich.console import Console
from rich.pretty import pprint
from rich.prompt import Confirm

__all__ = [
    "styled_print",
    "print_success",
    "print_cancelled",
    "exit_error",
    "ask_continue",
]


_console = Console(soft_wrap=True)


def styled_print(message: t.Any, end: str = "\n") -> None:  # pragma: no cover
    if isinstance(message, str):
        sub = "[bold hot_pink3]DevPilot[/]"
        message = message.replace("DevPilot", sub)
        _console.print(message, end=end)
    else:
        pprint(message, expand_all=True)


def print_success() -> None:  # pragma: no cover
    msg = "[chartreuse3] :heavy_check_mark: - Operation successful![/]"
    _console.print(msg, end="\n\n")


def print_cancelled() -> None:  # pragma: no cover
    msg = "[gold3] :warning: - Operation cancelled.[/]"
    _console.print(msg, end="\n\n")


def exit_error(reason: str) -> None:  # pragma: no cover
    msg = "[bold bright_red]:cross_mark: - DevPilot Error:[/]"
    reason = f"[bold bright_red]{reason}[/]"
    _console.print(msg, end="\n")
    _console.print(reason, end="\n\n")
    raise SystemExit(1)


def ask_continue() -> None:  # pragma: no cover
    answer = Confirm.ask("Do you want to continue?")
    if answer is False:
        print_cancelled()
        raise SystemExit(0)
