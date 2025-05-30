# SPDX-License-Identifier: LGPL-2.1-or-later

# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2025 Furgo                                              *
# *                                                                         *
# *   This file is part of FreeCAD.                                         *
# *                                                                         *
# *   FreeCAD is free software: you can redistribute it and/or modify it    *
# *   under the terms of the GNU Lesser General Public License as           *
# *   published by the Free Software Foundation, either version 2.1 of the  *
# *   License, or (at your option) any later version.                       *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful, but        *
# *   WITHOUT ANY WARRANTY; without even the implied warranty of            *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU      *
# *   Lesser General Public License for more details.                       *
# *                                                                         *
# *   You should have received a copy of the GNU Lesser General Public      *
# *   License along with FreeCAD. If not, see                               *
# *   <https://www.gnu.org/licenses/>.                                      *
# *                                                                         *
# ***************************************************************************

import Arch
from bimtests import TestArchBase

class TestArchCurtainWall(TestArchBase.TestArchBase):

    def test_makeCurtainWall(self):
        """Test the makeCurtainWall function."""
        operation = "Testing makeCurtainWall function"
        self.printTestMessage(operation)

        curtain_wall = Arch.makeCurtainWall(name="TestCurtainWall")
        self.assertIsNotNone(curtain_wall, "makeCurtainWall failed to create a curtain wall object.")
        self.assertEqual(curtain_wall.Label, "TestCurtainWall", "Curtain wall label is incorrect.")