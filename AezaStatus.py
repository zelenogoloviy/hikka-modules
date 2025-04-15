# MIT License
#
# Copyright (c) 2025 zelenogoloviy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ---------------------------------
# ---------------------------------------------------------------------------------
# Name: AezaStatus
# Description: Check availability of Aeza servers for rent.
# Author: @zelenogoloviy_m
# ---------------------------------------------------------------------------------
# meta developer: @zelenogoloviy_m
# scope: AezaStatus
# scope: AezaStatus 0.0.1
# ---------------------------------------------------------------------------------

import asyncio

from .. import loader, utils

__version__ = (0, 0, 1)


@loader.tds
class AezaStatus(loader.Module):
    """Check availability of Aeza servers for rent."""

    strings = {
        "name": "AezaStatus",
        "wait": "<emoji document_id=5328274090262275771>⏳</emoji> Wait...",
        "no_response": "<emoji document_id=5467928559664242360>❌</emoji> Error",
    }

    strings_ru = {
        "wait": "<emoji document_id=5328274090262275771>⏳</emoji> Подождите...",
        "no_response": "<emoji document_id=5467928559664242360>❌</emoji> Ошибка",
    }

    @loader.commands(
        ru_doc="Проверьте наличие свободных серверов Aeza для аренды.",
        en_doc="Check availability of Aeza servers for rent.",
    )
    async def status(self, message):
        msg = await utils.answer(message, self.strings["wait"])
        try:
            async with self.client.conversation("@aezastatus_bot") as conv:
                await conv.send_message("/status")
                resp = await conv.get_response()
                await utils.answer(msg, resp.text)
                await conv.mark_read()
                try:
                    await self.client.delete_messages(
                        "@aezastatus_bot", [resp.id, resp.id - 1]
                    )
                except:  # noqa: E722
                    pass
        except asyncio.TimeoutError:
            await utils.answer(msg, self.strings["no_response"])
