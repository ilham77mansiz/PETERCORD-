from userbot import BOT_USERNAME
from userbot.events import register

@register(outgoing=True, pattern="^.help")
async def yardim(event):
    tgbotusername = BOT_USERNAME
    if tgbotusername is not None:
        results = await event.client.inline_query(
            tgbotusername,
            "@PetercordIlhamMansiz"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.edit(LANG["NO_BOT"])
