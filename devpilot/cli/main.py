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

import importlib
import inspect
import typing as t
from pathlib import Path
from types import ModuleType

from typer import Typer

from devpilot import utils

app = Typer(
    name="devpilot", no_args_is_help=True, invoke_without_command=False, help=""
)


def find_command_modules() -> t.Generator[ModuleType, None, None]:
    package_path = utils.search_upwards("devpilot/__init__.py").parent
    import_dir = Path(__file__).with_name("commands")
    for filepath in import_dir.rglob("*.py"):
        relative_path = filepath.resolve().relative_to(package_path)
        module_path = ".".join(relative_path.with_suffix("").parts)
        yield importlib.import_module(package=package_path.name, name=f".{module_path}")


for module in find_command_modules():
    Members = t.List[t.Tuple[str, Typer]]
    for _, obj in t.cast(Members, inspect.getmembers(module)):
        if isinstance(obj, Typer):
            app.add_typer(typer_instance=obj, name=obj.info.name)
