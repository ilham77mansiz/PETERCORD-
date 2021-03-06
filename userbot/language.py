

from . import LANGUAGE, LOGS, bot, PLUGIN_CHANNEL_ID
from json import loads, JSONDecodeError
from os import path, remove
from telethon.tl.types import InputMessagesFilterDocument

pchannel = bot.get_entity(PLUGIN_CHANNEL_ID)
LOGS.info("Dara jangan kau bersedih...")
LANGUAGE_JSON = None

for dil in bot.iter_messages(pchannel, filter=InputMessagesFilterDocument):
    if ((len(dil.file.name.split(".")) >= 2) and (
            dil.file.name.split(".")[1] == "masterjson")):
        if path.isfile(f"./userbot/language/{dil.file.name}"):
            try:
                LANGUAGE_JSON = loads(
                    open(
                        f"./userbot/language/{dil.file.name}",
                        "r").read())
            except JSONDecodeError:
                dil.delete()
                remove(f"./userbot/language/{dil.file.name}")

                if path.isfile("./userbot/language/DEFAULT.masterjson"):
                    LOGS.warn("Menggunakan file bahasa default...")
                    LANGUAGE_JSON = loads(
                        open(
                            f"./userbot/language/DEFAULT.masterjson",
                            "r").read())
                else:
                    raise Exception("Your language file is invalid")
        else:
            try:
                DOSYA = dil.download_media(file="./userbot/language/")
                LANGUAGE_JSON = loads(open(DOSYA, "r").read())
            except JSONDecodeError:
                dil.delete()
                if path.isfile("./userbot/language/DEFAULT.masterjson"):
                    LOGS.warn("Varsayılan dil dosyası kullanılıyor...")
                    LANGUAGE_JSON = loads(
                        open(
                            f"./userbot/language/DEFAULT.masterjson",
                            "r").read())
                else:
                    raise Exception("Your language file is invalid")
        break

if LANGUAGE_JSON is None:
    if path.isfile(f"./userbot/language/{LANGUAGE}.masterjson"):
        try:
            LANGUAGE_JSON = loads(
                open(
                    f"./userbot/language/{LANGUAGE}.masterjson",
                    "r").read())
        except JSONDecodeError:
            raise Exception("Invalid json file")
    else:
        if path.isfile("./userbot/language/DEFAULT.masterjson"):
            LOGS.warn("Varsayılan dil dosyası kullanılıyor...")
            LANGUAGE_JSON = loads(
                open(
                    f"./userbot/language/DEFAULT.masterjson",
                    "r").read())
        else:
            raise Exception(f"Didn't find {LANGUAGE} file")

LOGS.info(f"{LANGUAGE_JSON['LANGUAGE']} dili yüklendi.")


def get_value(plugin=None, value=None):
    global LANGUAGE_JSON

    if LANGUAGE_JSON is None:
        raise Exception("Please load language file first")
    else:
        if plugin is not None or value is None:
            Plugin = LANGUAGE_JSON.get("STRINGS").get(plugin)
            if Plugin is None:
                raise Exception("Invalid plugin")
            else:
                String = LANGUAGE_JSON.get("STRINGS").get(plugin).get(value)
                if String is None:
                    return Plugin
                else:
                    return String
        else:
            raise Exception("Invalid plugin or string")
