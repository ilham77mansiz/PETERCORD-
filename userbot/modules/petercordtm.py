# BASED FROM ULTROID PORTED FOR PETERCORD USERBOT BY MANSIEZ / @diemmmmmmmmmm
# THANKS ULTROID
# DONT REMOVE THIS
# TENTANG AKU DAN DIA
# @petercord

from telethon import events
from userbot import bot
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r"^\.tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    lord = await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await lord.edit("`Mohon buka blokir` @TempMailBot `lalu coba lagi`")
            return
        await event.edit(f"**PETERCORD TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({PETERCORDUSERBOT})")


# TENTANG AKU DAN DIA
# Ported For Petercord Userbot From Ultroid

CmdHelp('petercordtm').add_command('tm', '<alamat email>',
                                   'Untuk mendapatkan Tempail email.').add()
