from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.hentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @nHentaiBot and try again```")
            return
        if response.text.startswith("**Sorry I couldn't get manga from**"):
            await event.edit("```I think this is not the right link```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)

CmdHelp('hentai').add_command(
    'filters', None, 'Bir sohbetteki tüm userbot filtrelerini listeler.'
).add_command(
    'filter', '<filtrelenecek kelime> <cevaplanacak metin> ya da bir mesajı .filter <filtrelenecek kelime>', 'Filtre ekler. Ne zaman eklediğiniz kelime/cümle yazılırsa bot cevap verir.', '.filter "merhaba" "meraba"'
).add_command(
    'stop', '<filtre>', 'Seçilen filtreyi durdurur.'
).add_command(
    'genelfilter', '<filtrelenecek kelime> <cevaplanacak metin> ya da bir mesajı .genelfilter <filtrelenecek kelime>', 'Genel filtre ekler. Tüm gruplarda çalışır.'
).add_command(
    '.genelstop', '<filtre>', 'Seçilen genel filtreyi durdurur.'
).add()
