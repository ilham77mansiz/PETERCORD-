# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import pyfiglet
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r"^\.fg(?: |$)(.*)")
async def figlet(e):
    if e.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital"}
    input_str = e.pattern_match.group(1)
    if "." in input_str:
        text, cmd = input_str.split(".", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await e.edit("`Please add some text to figlet`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await e.edit("`Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await e.respond("‌‌‎`{}`".format(result))
    await e.delete()

CmdHelp('adzan').add_command(
    'adzan', '<kota> <daerah>', 'Untuk menampilkan waktu sholat di kota yang telah di tentukan.'
).add()
