from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.perintah(?: |$)(.*)")
async def master(event):
    """ .master ketik """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Tolong.. Ketik gunakan dengan benar kata modulenya:)")
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5]
                 for i in range(0, len(sorted(list(CMD_HELP))), 5)]

        for i in sayfa:
            string += f'`⚡ `'
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.edit("PETERCORD" + '\n\n' + string)
