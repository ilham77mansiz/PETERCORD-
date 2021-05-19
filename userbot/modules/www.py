# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import ALIVE_NAME, StartTime
from userbot.events import register
import time
from userbot.cmdhelp import CmdHelp


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██")
    await pong.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█ \n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█ \n██████▄▄█‡‡‡‡‡‡████████▄ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█ \n▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██ \n█████‡‡‡‡‡‡‡██████████")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f" • 𝐒𝐈𝐍𝐘𝐀𝐋 "
                    f"\n  ➢ `%sms` \n"
                    f" • 𝐎𝐖𝐍𝐄𝐑 "
                    f"\n  ➢ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Love Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✣ PONG!**\n"
                    f"❦ **Ping:** "
                    f"`%sms` \n"
                    f"❦ **Uptime:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⌖ Pong!**\n"
                    f"➠ __Ping:__ "
                    f"`%sms` \n"
                    f"➠ __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("...➡")
    await pong.edit("➡.......")
    await pong.edit("⬇")
    await pong.edit("☯")
    await pong.edit("Shaoloin....")
    await pong.edit("..DuaRR...")
    await pong.edit("☯..\n ADA BOMS💣")
    await pong.edit("**💣**")
    await pong.edit("**💥**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━《 **𝗣 𝗘 𝗧 𝗘 𝗥 𝗖 𝗢 𝗥 𝗗** 》━\n"
                    f"┣➠  __Ping:__ "
                    f"`%sms` \n"
                    f"┗➠ __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀 Pusshhh...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "🕸 **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n"
                   "🕸 **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "🕸 **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "🕸 **Ping:** "
                   f"`{result['ping']}` \n"
                   "🕸 **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "🕸 **BOT:** `Petercord Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("LABA-LABA SPIDERMAN🕷!.....🕸")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("- 🕸P E T E R C O R D 🕸 -\n`%sms`" % (duration))

CmdHelp('www').add_command(
    'speed', None, 'Melakukan speedtest dan menampilkan hasilnya.'
).add_command(
    'dc', None, 'Menampilkan pusat data yang paling dekat dengan server Anda.'
).add_command(
    'ping', None, 'Menunjukkan nilai ping bot.'
).add_command(
    'pong', None, 'Menunjukkan nilai pong bot.'
).add_command(
    'xping', None, 'Menunjukkan nilai ping bot.'
).add_command(
    'lping', None, 'Menunjukkan nilai ping bot.'
).add()
