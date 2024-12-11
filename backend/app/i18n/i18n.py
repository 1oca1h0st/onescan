import os

from babel.support import Translations

from app.env import BASE_DIR

TRANSLATIONS = {
    "zh_CN": Translations.load(os.path.join(BASE_DIR, "i18n/langs"), locales=["zh_CN"]),
    "en_US": Translations.load(os.path.join(BASE_DIR, "i18n/langs"), locales=["en_US"]),
}

translations = TRANSLATIONS.get("en_US")


def set_locale(locale: str):
    global translations
    translations = TRANSLATIONS.get(locale) or TRANSLATIONS.get("en_US")
    translations.install(locale)
    print(os.path.join(BASE_DIR, "i18n/langs"))


def _(msg: str):
    return translations.ugettext(msg)
