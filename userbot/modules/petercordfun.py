# Based Plugins
# Ported For Petercord-Userbot By bismillahselaluadaa/Ilham
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini!!!
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()

# ILham Mansiezz


@register(outgoing=True, pattern=r"^\.game(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@inlinegamesbot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()

# ILham Mansiezz


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Ported For Petercord-Userbot By bismillahselaluadaa/ILham

CmdHelp('petercordgame').add_command('game', None,
                                     'menampilkan game via bot.').add()
