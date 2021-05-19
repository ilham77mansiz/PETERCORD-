import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from . import BOT_VER, BRAIN_CHECKER, LOGS, PLUGIN_CHANNEL_ID, bot
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from telethon.tl import functions

from random import choice
import re
import userbot.cmdhelp

DIZCILIK_STR = [
    "Saya meratakan stiker...",
    "Hidup melesat...",
    "Saya mengundang stiker ini ke paket saya sendiri...",
    "Saya perlu memperbaikinya...",
    "Hei, ini stiker yang bagus!\nSaya sedang meluruskan..",
    "Saya meratakan stiker Anda\nhahaha.",
    "Hei lihat di sana. (☉｡☉)!→\nSelagi aku mengatakan ini...",
    "Mawar merah violet biru, saya akan keren dengan menempelkan stiker ini di paket saya...",
    "Jailbreak stiker...",
    "Master orang asing menyanyikan stiker ini... ",
]

AFKSTR = [
    "Saya sedang terburu-buru sekarang, tidak bisakah Anda mengirim pesan nanti?  Saya akan datang lagi.",
    "Orang yang Anda panggil tidak dapat menjawab telepon sekarang. Anda dapat meninggalkan pesan Anda dengan tarif Anda sendiri setelah nada. Biaya pesan 49 kurus.\n`biiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Aku akan kembali dalam beberapa menit. Tapi jika tidak ... tunggu lebih lama.",
    "Saya tidak di sini sekarang, saya mungkin di tempat lain.",
    "Mawar itu merah\nMawar berwarna biru\nTinggalkan aku pesan\nDan aku akan menghubungi kamu kembali.",
    "Terkadang hal terbaik dalam hidup pantas untuk ditunggu…\nAku akan segera kembali.",
    "Saya akan segera kembali, tetapi jika saya tidak kembali, saya akan kembali lagi nanti.",
    "Jika Anda belum mengerti, saya tidak di sini.",
    "Halo, selamat datang di pesan jauh saya, bagaimana saya bisa mengabaikan Anda hari ini?",
    "Saya jauh dari 7 lautan dan 7 negara,\n7 perairan dan 7 benua,\n7 gunung dan 7 bukit,\n7 dataran dan 7 gundukan,\n7 kolam dan 7 danau,\n7 mata air dan 7 padang rumput,\n7 kota dan 7 lingkungan,\n7 blok dan 7 rumah ...\n\nTempat di mana bahkan pesan tidak bisa sampai ke saya! ",
    "Saya jauh dari keyboard sekarang, tetapi jika Anda berteriak cukup keras di layar Anda, saya dapat mendengar Anda.",
    "Saya bergerak ke arah berikut\n ---->",
    "Saya bergerak ke arah berikut\n <----",
    "Silakan tinggalkan pesan dan buat saya merasa lebih penting daripada sebelumnya.",
    "Pemilik saya tidak ada di sini, jadi berhentilah menulis kepada saya.",
    "Jika aku ada di sini,\nAku akan memberitahumu di mana aku berada.\n\nTapi bukan aku,\\ketika aku kembali tanyakan padaku ...",
    "Saya pergi!\nSaya tidak tahu kapan saya akan kembali!\nSaya berharap beberapa menit kemudian!",
    "Pemilik saya tidak ada saat ini. Jika Anda memberikan nama, nomor dan alamat Anda, saya dapat mengirimkannya kepadanya dan begitu dia kembali.",
    "Maaf, pemilik saya tidak ada di sini. Anda dapat berbicara dengan saya sampai dia datang.\ndia pemilik akan kembali kepada Anda nanti.",
    "Saya yakin Anda mengharapkan pesan!",
    "Hidup ini terlalu singkat, banyak yang harus dilakukan ...\nAku melakukan salah satunya ...",
    "Aku tidak disini sekarang ....\ntapi jika aku ...\n\nbukankah itu bagus?",
]

UNAPPROVED_MSG = (
    "`Hei,` {mention`! Ini bot. Jangan khawatir.\n\n`"
    "`Pemilik saya belum memberi Anda izin kepada PM.`"
    "`Harap tunggu pemilik saya aktif, dia biasanya akan mengkonfirmasi PM.\n\n`"
    "`Sejauh yang saya tahu, dia tidak mengizinkan orang untuk PM secara singkat.")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nHATA: Girilen telefon numarası geçersiz' \
             '\n  Ipucu: Ülke kodunu kullanarak numaranı gir' \
             '\n       Telefon numaranızı tekrar kontrol edin'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()


def extractCommands(file):
    FileRead = open(file, 'r').read()

    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # PetercordPY
            Petercordpy = re.search(
                '\"\"\"PETERCORDPY(.*)\"\"\"', FileRead, re.DOTALL)
            if Petercordpy is not None:
                Petercordpy = Petercordpy.group(0)
                for Satir in Petercordpy.splitlines():
                    if ('"""' not in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]

                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(
                    Komut,
                    None,
                    'Bu plugin dışarıdan yüklenmiştir. Herhangi bir açıklama tanımlanmamıştır.')
            CmdHelp.add()


try:
    bot.start()
    idim = bot.get_me().id
    masterbl = requests.get(
        'https://gitlab.com/Quiec/asen/-/raw/master/asen.json').json()
    if idim in masterbl:
        bot.disconnect()

    # ChromeDriver'ı Ayarlayalım #
    try:
        chromedriver_autoinstaller.install()
    except BaseException:
        pass


for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    "Pesanmu sedang berjalan! Uji dengan mengetik .alive di obrolan apa pun."
    " Jika Anda membutuhkan bantuan, datanglah ke grup Dukungan kami https://t.me/TEAMSquadUserbotSupport")
LOGS.info(f"Bot Version: PETERCORD USERBOT {BOT_VER}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
