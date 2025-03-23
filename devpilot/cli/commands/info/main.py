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

import site
import typing as t
from pathlib import Path

from typer import Typer

from devpilot.cli import console

app = Typer(name="info", no_args_is_help=False, invoke_without_command=True, help="")


@app.callback()
def callback() -> None:
    title_color = "#ff5fff"
    key_color = "#87d7d7"
    value_color = "#ffd787"

    console.styled_print(f"[{title_color}]Package Info:[/]")
    for k, v in PackageInfo().items():
        k = f"[{key_color}]{k}[/]"
        v = f"[{value_color}]{v}[/]"
        console.styled_print(f"{2 * ' '}{k}: {v}")


class PackageInfo(t.Dict[str, t.Optional[str]]):
    _PACKAGE_NAME = "devpilot"
    Name: str
    Version: str
    Summary: str
    License: str
    Author: str
    Homepage: str

    def __init__(self) -> None:
        super().__init__()
        for site_dir in site.getsitepackages():
            if "site-packages" not in site_dir:  # pragma: no cover
                continue
            for child in Path(site_dir).iterdir():
                is_self_pkg = child.name.startswith(self._PACKAGE_NAME)
                if not is_self_pkg or child.suffix != ".dist-info":
                    continue
                meta = child / "METADATA"
                with meta.open("r") as file:
                    lines = file.readlines()
                self._set_fields(lines)

    def _set_fields(self, lines: t.List[str]) -> None:
        for line in lines:  # pragma: no branch
            if line.startswith("\n"):
                break
            k, v = line.split(": ", maxsplit=1)
            if k in ["Name", "Version", "Summary"]:
                self[k] = v.rstrip()
            elif k == "License-Expression":
                self["License"] = v.rstrip()
            elif k == "Author-email":
                self["Author"] = v.rstrip()
            elif v.startswith("Repository"):
                self["Homepage"] = v.split(", ")[1].rstrip()

    def __getattr__(self, name: str) -> t.Optional[str]:
        if name in self:
            return self[name]
        return None
