# The source code was taken from software "H", available via link: https://mods.codwiz.life/H.py.
# Proprietary License Agreement

# Copyright (c) 2024-29 CodWiz

# Permission is hereby granted to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for personal and non-commercial purposes, subject to the following conditions:

# 1. The Software may not be modified, altered, or otherwise changed in any way without the explicit written permission of the author.

# 2. Redistribution of the Software, in original or modified form, is strictly prohibited without the explicit written permission of the author.

# 3. The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

# 4. Any use of the Software must include the above copyright notice and this permission notice in all copies or substantial portions of the Software.

# 5. By using the Software, you agree to be bound by the terms and conditions of this license.

# For any inquiries or requests for permissions, please contact codwiz@yandex.ru.
# ---------------------------------------------------------------------------------
# Name: Z
# Description: Z
# Author: @zelenogoloviy_m
# ---------------------------------------------------------------------------------
# meta developer: @zelenogoloviy_m
__version__ = (0, 2, 0)
#imports
from .. import loader, utils

#class
@loader.tds
class z(loader.Module):
    """z"""
    strings = {"name": "З", "z": "З"}
    strings_en = {"name": "Z", "z": "Z"}

    @loader.command(
        en_doc="Z",
    )
    #function
    async def z(self, message):
        """З"""
        #З
        await utils.answer(message, self.strings("z"))
