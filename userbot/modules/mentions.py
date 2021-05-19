import re

from telethon.tl import types

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")


@register(outgoing=True, ignore_unsafe=True, disable_errors=True)
async def mention(event):
    newstr = event.text
    if event.entities:
        newstr = nameexp.sub(r'<a href="tg://user?id=\2">\3</a>', newstr, 0)
        for match in usernexp.finditer(newstr):
            user = match.group(1)
            text = match.group(2)
            name, entities = await bot._parse_message_text(text, "md")
            rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
            if entities:
                for e in entities:
                    tag = None
                    if isinstance(e, types.MessageEntityBold):
                        tag = "<b>{}</b>"
                    elif isinstance(e, types.MessageEntityItalic):
                        tag = "<i>{}</i>"
                    elif isinstance(e, types.MessageEntityCode):
                        tag = "<code>{}</code>"
                    elif isinstance(e, types.MessageEntityStrike):
                        tag = "<s>{}</s>"
                    elif isinstance(e, types.MessageEntityPre):
                        tag = "<pre>{}</pre>"
                    elif isinstance(e, types.MessageEntityUnderline):
                        tag = "<u>{}</u>"
                    if tag:
                        rep = tag.format(rep)
            newstr = re.sub(re.escape(match.group(0)), rep, newstr)
    if newstr != event.text:
        await event.edit(newstr, parse_mode="html")


CmdHelp('mention').add_command(
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
