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

from devpilot import utils
from devpilot.cli.commands.info.main import PackageInfo

from .conftest import CliRunner


def test_info_command() -> None:
    path = utils.search_upwards("pyproject.toml")
    data = rtoml.load(path)

    exit_code, stdout = CliRunner.info_app().invoke()
    assert exit_code == 0 and "Package Info" in stdout

    match = re.search(r"Name: (\w+)", stdout)
    assert match and match.group(1) == data["project"]["name"]

    match = re.search(r"Version: ([\w.]+)", stdout)
    assert match and match.group(1) == data["project"]["version"]

    match = re.search(r"Summary: ([\w,. ]+)", stdout)
    assert match and match.group(1) == data["project"]["description"]

    match = re.search(r"Homepage: ([\w:./]+)", stdout)
    assert match and match.group(1) == data["project"]["urls"]["Repository"]

    match = re.search(r"Author: ([\w<>@. ]+)", stdout)
    a_name, a_email = data["project"]["authors"][0].values()
    assert match and match.group(1) == f"{a_name} <{a_email}>"

    match = re.search(r"License: ([\w\-.]+)", stdout)
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
