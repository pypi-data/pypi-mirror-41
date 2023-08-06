#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Snippy - command, solution, reference and code snippet manager.
#  Copyright 2017-2019 Heikki J. Laaksonen  <laaksonen.heikki.j@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""api_snippets: JSON REST API for Snippets."""

from snippy.constants import Constants as Const
from snippy.server.rest.base import ApiContentBase
from snippy.server.rest.base import ApiContentDigestBase
from snippy.server.rest.base import ApiContentDigestFieldBase


class ApiSnippets(ApiContentBase):
    """Query snippets."""

    def __init__(self, content):
        super(ApiSnippets, self).__init__(content, Const.SNIPPET)


class ApiSnippetsDigest(ApiContentDigestBase):
    """Query snippets based on digest."""

    def __init__(self, content):
        super(ApiSnippetsDigest, self).__init__(content, Const.SNIPPET)


class ApiSnippetsField(ApiContentDigestFieldBase):
    """Query snippets based on digest and specified field."""

    def __init__(self, content):
        super(ApiSnippetsField, self).__init__(content, Const.SNIPPET)
