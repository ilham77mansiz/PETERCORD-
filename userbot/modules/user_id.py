from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r"^\.getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Balas Ke Pesan Petercord`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Mohon Balas Ke Pesan Petercord```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Mohon Balas Ke Pesan Petercord`")
        return
    await event.edit("`Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Sedang Error`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Petercord Orang Ini Tidak Mempunyai ID`")
        else:
            await event.edit(f"{response.message.message}")


CmdHelp('getid').add_command(
    'getid', None, 'Replay ke pengguna untuk mendapatkan id user.'
).add()
