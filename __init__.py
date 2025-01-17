"""
@author: Julian Adventurer.
@title: Wild Divide
@nickname: WildDivide
@description: This node is used to encode a wildcard string.
"""

import os
from . import wildcard_server

from .wild_divide import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

try:
    import cm_global

    cm_global.register_extension(
        "WildDivide",
        {
            "version": "0.1.0",
            "name": "Wild Divide",
            "nodes": set(NODE_CLASS_MAPPINGS.keys()),
            "description": "This extension provides the ability to build prompts using wildcards for each region of a split image.",
        },
    )
except:
    pass
