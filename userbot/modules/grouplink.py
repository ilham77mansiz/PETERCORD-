#

from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern="^.gsend ?(.*)")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("`Pesan Di Di Teruskan Ke Grup Tujuan`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("Pesan Di Di Teruskan Ke Grup Tujuan`")
    except BaseException:
        await event.edit("** Gagal Mengirim Pesan, Emang Lu Join Grup Nya Njing ? **")

CmdHelp('filter').add_command(
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
