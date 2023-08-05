# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

from __future__ import absolute_import
from __future__ import print_function

import os
import shutil
import tempfile

from twisted.trial import unittest

from buildbot.test.util.decorators import skipUnlessPlatformIs
from buildbot.util.private_tempdir import PrivateTemporaryDirectory


class TestTemporaryDirectory(unittest.TestCase):
    # In this test we want to also check potential platform differences, so
    # we don't mock the filesystem access

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_simple(self):
        dir = os.path.join(self.tempdir, 'simple')

        with PrivateTemporaryDirectory(dir):
            self.assertTrue(os.path.isdir(dir))
        self.assertFalse(os.path.isdir(dir))

    @skipUnlessPlatformIs('posix')
    def test_mode(self):
        dir = os.path.join(self.tempdir, 'mode')

        with PrivateTemporaryDirectory(dir, mode=0o700):
            self.assertEqual(0o40700, os.stat(dir).st_mode)

    def test_already_exists(self):
        dir = os.path.join(self.tempdir, 'already_exists')

        os.makedirs(dir)
        with self.assertRaises(Exception):
            with PrivateTemporaryDirectory(dir):
                pass
        shutil.rmtree(dir)

    def test_cleanup(self):
        dir = os.path.join(self.tempdir, 'cleanup')

        with PrivateTemporaryDirectory(dir) as ctx:
            self.assertTrue(os.path.isdir(dir))
            ctx.cleanup()
            self.assertFalse(os.path.isdir(dir))
            ctx.cleanup()  # also check whether multiple calls don't throw
            ctx.cleanup()
