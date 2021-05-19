import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r'^.kekuatan(:? |$)([1-8])?')
async def _(fry):
    await fry.edit("`Petercord Mengaktifkan Kekuatan Telegram...👾`")
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await fry.edit("`Mohon Balas Di Sticker Petercord`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`Gambar tidak di dukung`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Mohon Balas Di Sticker Petercord`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with fry.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.reply("`Petercord Mohon Unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await fry.edit("`Petercord Mohon Matikan Setelan Forward Privasi...`")
        else:
            downloaded_file_name = await fry.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await fry.client.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await fry.client.delete_messages(conv.chat_id,
                                                 [msg.id, response.id])
            else:
                await fry.client.delete_messages(
                    conv.chat_id,
                    [msg.id, response.id, r.id, msg_level.id])
    await fry.delete()
    return os.remove(downloaded_file_name)


@register(outgoing=True, pattern=r'^.df(:? |$)([1-8])?')
async def _(fry):
    await fry.edit("`Sedang Dalam Proses......`")
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await fry.edit("`Mohon Balas Di Sticker Petercord`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`Mohon Balas Di Sticker Petercord`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Mohon Balas Di Sticker Petercord`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with fry.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.reply("`Petercord Mohon Unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await fry.edit("`Petercord Mohon Matikan Setelan Privasi Forward...`")
        else:
            downloaded_file_name = await fry.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await fry.client.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await fry.client.delete_messages(conv.chat_id,
                                                 [msg.id, response.id])
            else:
                await fry.client.delete_messages(
                    conv.chat_id,
                    [msg.id, response.id, r.id, msg_level.id])
    await fry.delete()
    return os.remove(downloaded_file_name)


CmdHelp('kekuatan').add_command(
    'filters',
    None,
    'Bir sohbetteki tüm userbot filtrelerini listeler.').add_command(
        'filter',
        '<filtrelenecek kelime> <cevaplanacak metin> ya da bir mesajı .filter <filtrelenecek kelime>',
        'Filtre ekler. Ne zaman eklediğiniz kelime/cümle yazılırsa bot cevap verir.',
        '.filter "merhaba" "meraba"').add_command(
            'stop',
            '<filtre>',
            'Seçilen filtreyi durdurur.').add_command(
                'genelfilter',
                '<filtrelenecek kelime> <cevaplanacak metin> ya da bir mesajı .genelfilter <filtrelenecek kelime>',
                'Genel filtre ekler. Tüm gruplarda çalışır.').add_command(
                    '.genelstop',
                    '<filtre>',
    'Seçilen genel filtreyi durdurur.').add()
