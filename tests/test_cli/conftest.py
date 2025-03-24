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

from __future__ import annotations

import typing as t
from dataclasses import dataclass

from rich.text import Text
from typer import Typer
from typer.testing import CliRunner as TyperCliRunner

from devpilot.cli.commands.chglog.main import app as chglog_app
from devpilot.cli.commands.docker.main import app as docker_app
from devpilot.cli.commands.info.main import app as info_app
from devpilot.cli.commands.init.main import app as init_app
from devpilot.cli.commands.license.main import app as license_app
from devpilot.cli.commands.version.main import app as version_app
from devpilot.cli.main import app as main_app


@dataclass(frozen=True)
class CliRunner:
    cmd_args: t.Union[str, t.Sequence[str], None]
    user_input: t.Union[bytes, str, t.IO, None]
    runner: TyperCliRunner
    app: Typer
    debug: bool

    def invoke(self) -> t.Tuple[int, str]:
        result = self.runner.invoke(self.app, self.cmd_args, self.user_input)
        clean_output = Text.from_ansi(result.stdout).plain
        if self.debug:
            print("\n===== CONSOLE OUTPUT BEGIN ====")
            print(clean_output)
            print("===== CONSOLE OUTPUT END ====\n")
        return result.exit_code, clean_output

    def expect_success(self) -> str:
        exit_code, clean_output = self.invoke()
        assert exit_code == 0 and "Operation successful" in clean_output
        return clean_output

    def expect_cancelled(self) -> str:
        exit_code, clean_output = self.invoke()
        assert exit_code == 0 and "Operation cancelled" in clean_output
        return clean_output

    def expect_error(self) -> str:
        exit_code, clean_output = self.invoke()
        assert exit_code == 1 and "DevPilot Error" in clean_output
        return clean_output

    @classmethod
    def main_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=main_app,
            debug=debug,
        )

    @classmethod
    def chglog_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=chglog_app,
            debug=debug,
        )

    @classmethod
    def docker_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=docker_app,
            debug=debug,
        )

    @classmethod
    def info_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=info_app,
            debug=debug,
        )

    @classmethod
    def init_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=init_app,
            debug=debug,
        )

    @classmethod
    def license_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=license_app,
            debug=debug,
        )

    @classmethod
    def version_app(
        cls,
        cmd_args: t.Union[str, t.Sequence[str], None] = None,
        user_input: t.Union[bytes, str, t.IO, None] = None,
        debug: bool = False,
    ) -> CliRunner:
        return cls(
            cmd_args=cmd_args,
            user_input=user_input,
            runner=TyperCliRunner(),
            app=version_app,
            debug=debug,
        )
