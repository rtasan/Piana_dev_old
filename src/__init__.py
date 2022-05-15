# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import auto_load
from .tools import injector
import bpy
bl_info = {
    "name": "Piana",
    "author": "Luviana",
    "description": "",
    "blender": (2, 93, 0),
    "version": (0, 0, 1),
    "location": "3D View > Tools",
    "warning": "",
    "category": "Import-Export",
    "support": "COMMUNITY",
}


auto_load.init()


def register():
    auto_load.register()
    injector.inject_dll(addon_prefs = bpy.context.preferences.addons[__package__].preferences)


def unregister():
    auto_load.unregister()
