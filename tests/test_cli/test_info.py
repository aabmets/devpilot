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

import re

import rtoml
from rich.text import Text
from typer.testing import CliRunner

from devpilot import utils
from devpilot.cli.commands.info.main import PackageInfo, app


def test_info_command() -> None:
    path = utils.search_upwards("pyproject.toml")
    data = rtoml.load(path)

    runner = CliRunner()
    result = runner.invoke(app)
    clean_text = Text.from_ansi(result.stdout).plain

    assert result.exit_code == 0
    assert "Package Info" in clean_text

    match = re.search(r"Name: (\w+)", clean_text)
    assert match and match.group(1) == data["project"]["name"]

    match = re.search(r"Version: ([\w.]+)", clean_text)
    assert match and match.group(1) == data["project"]["version"]

    match = re.search(r"Summary: ([\w,. ]+)", clean_text)
    assert match and match.group(1) == data["project"]["description"]

    match = re.search(r"Homepage: ([\w:./]+)", clean_text)
    assert match and match.group(1) == data["project"]["urls"]["Repository"]

    match = re.search(r"Author: ([\w<>@. ]+)", clean_text)
    a_name, a_email = data["project"]["authors"][0].values()
    assert match and match.group(1) == f"{a_name} <{a_email}>"

    match = re.search(r"License: ([\w\-.]+)", clean_text)
    assert match and match.group(1) == data["project"]["license"]


def test_package_info() -> None:
    path = utils.search_upwards("pyproject.toml")
    data = rtoml.load(path)
    info = PackageInfo()

    assert info.Name == data["project"]["name"]
    assert info.Version == data["project"]["version"]
    assert info.Summary == data["project"]["description"]
    assert info.Homepage == data["project"]["urls"]["Repository"]
    a_name, a_email = data["project"]["authors"][0].values()
    assert info.Author == f"{a_name} <{a_email}>"
    assert info.License == data["project"]["license"]
    assert info.NonExistantAttribute is None
