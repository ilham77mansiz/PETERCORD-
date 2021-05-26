from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest
from userbot import *
from userbot.cmdhelp import *


def button(page, modules):
    Row = 5
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i: i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
    f"🎖 " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"◀️ ᏴᎪᏟᏦ 🎖", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"•🎖 ❌ 🎖•", data="close"
            ),
            custom.Button.inline(
               f"🎖 ΝᎬХͲ ▶️", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id


@ tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.reply("Petercord-Userbot, Buat Userbot Mu Sendiri [Tekan Disini](https://github.com/ilham77mansiz/-PETERCORD-.git)")
            else:
                await event.reply(f"`Hai Petercord {ALIVE_NAME}\n\nApa Kabarmu?`")

        @ tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@UserButt"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.article(
                    "Harap Gunakan .help Untuk Perintah",
                    text="{}\n\n**⚡ Jumlah Modul:** `{}`\n               \n**⚡ Daftar Modul  PETERCORD-USERBOT:\n\n╰┄┅┷┅┄┄┅┷┅┄╯** \n".format(
                        "**╭┄┅┯┅┄┄┅┯┅┄╮\n\n⚡PETERCORD-USERBOT**",
                        len(dugmeler),
                    ),
                    buttons=buttons,
                    link_preview=False,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan PETERCORD⚖USERBOT ",
                    text="Daftar Modul",
                    buttons=[],
                    link_preview=True)
            else:
                result = builder.article(
                    "**🎖PETERCORD USERBOT🎖**",
                    text="""**Anda Bisa Membuat 🎖PETERCORD USERBOT🎖 Anda Sendiri Dengan Cara:** [GABUNG DISINI](https://t.me/TEAMSquadUserbotSupport)""",
                    buttons=[
                        [
                            custom.Button.url(
                                "🎖REPO PETERCORD🎖",
                                "https://github.com/ilham77mansiz/-PETERCORD-"),
                            custom.Button.url(
                                "INSTAGRAM",
                                "https://www.instagram.com/imansiez77/"),
                            custom.Button.url(
                                "OWNERS",
                                "t.me/diemmmmmmmmmm")],
                    ],
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\\((.+?)\\)")))
    async def page(event):
        if not event.query.user_id == uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN MAFIABOT AND USE. © MafiaBot ™",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Legenday AF** [MafiaBot](https://t.me/MafiaBot_Support) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == uid:
            await delete_mafia(event,
              "👑MafiaBot Menu Provider Is now Closed👑\n\n         **[© MafiaBot ™](t.me/MafiaBot_Support)**", 5, link_preview=False
            )
        else:
                reply_pop_up_alert = f"Harap Deploy Petercord Userbot Anda Sendiri, Jangan Menggunakan Milik Petercord {ALIVE_NAME} ツ"

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN MAFIABOT AND USE. © MafiaBot ™",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "⚡ " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏴᎪᏟᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN MAFIABOT AND USE. © MafiaBot ™",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀️ ᏴᎪᏟᏦ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
