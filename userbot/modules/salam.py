from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum warahmatullahi Bismillah cari teman ada yang mau gak?")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum warahmatullahi wb😊")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam Semoga bermanfaat salamnya")


CmdHelp('adzan').add_command(
    'adzan', '<kota> <daerah>', 'Untuk menampilkan waktu sholat di kota yang telah di tentukan.'
).add()
