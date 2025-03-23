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
from functools import cache
from pathlib import Path


@cache
def search_upwards(
    for_path: t.Union[str, Path], from_path: t.Union[str, Path] = __file__
) -> Path:
    current_path = Path(from_path).parent.resolve()
    while current_path != current_path.parent:
        search_path = current_path / for_path
        if search_path.exists():
            return search_path
        elif (current_path / ".git").exists():
            break
        current_path = current_path.parent
    raise RuntimeError(f"Cannot find path '{for_path}' upwards from '{from_path}'")
