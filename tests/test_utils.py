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

import secrets
from pathlib import Path

import pytest

from devpilot import utils


def test_search_upwards() -> None:
    path = utils.search_upwards("tests")
    assert path == Path(__file__).resolve().parent
    assert isinstance(path, Path)

    bad_path = secrets.token_hex()
    with pytest.raises(RuntimeError):
        utils.search_upwards(bad_path, __file__)
    with pytest.raises(RuntimeError):
        utils.search_upwards(bad_path, path.parent)
