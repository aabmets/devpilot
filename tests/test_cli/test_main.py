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

from .conftest import CliRunner


def test_main() -> None:
    exit_code, stdout = CliRunner.main_app().invoke()

    assert exit_code == 0
    assert "Usage: devpilot" in stdout
    assert "chglog" in stdout
    assert "docker" in stdout
    assert "info" in stdout
    assert "init" in stdout
    assert "license" in stdout
    assert "version" in stdout
