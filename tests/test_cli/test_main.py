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

from typer.testing import CliRunner

from devpilot.cli.main import app


def test_main() -> None:
    runner = CliRunner()
    result = runner.invoke(app)

    assert result.exit_code == 0
    assert "Usage: devpilot" in result.stdout
    assert "chglog" in result.stdout
    assert "docker" in result.stdout
    assert "info" in result.stdout
    assert "init" in result.stdout
    assert "license" in result.stdout
    assert "version" in result.stdout
