#credits: mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types
from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern="^.gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Petercord Mohon Berikan Tempat Yang Dicari`")

    await event.edit("`Menemukan Lokasi Ini Di Server Map....`")

    geolocator = Nominatim(user_agent="Petercord")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("`Petercord Saya Tidak Dapat Menemukannya`")

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
