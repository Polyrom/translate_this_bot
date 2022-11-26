from emoji import emojize

START = emojize(':handshake_light_skin_tone_dark_skin_tone: '
                'Выберите языковую пару, '
                'а затем пришлите мне слово или простое словосочетание, чтобы получить '
                'перевод и примеры использования! :slightly_smiling_face:')

HELP = emojize('"Translate This!" – бот для перевода слов '
               'и простых словосочетаний.\n\n'
               'По умолчанию бот переводит с английского на русский.'
               'Чтобы выбрать другую языковую пару, отправьте мне команду\n /picklanguages, '
               'а затем напишите мне слово или простое словосочетание, '
               'чтобы получить перевод и примеры использования! :slightly_smiling_face:')

PICK_SOURCE = 'С какого языка переводим?'

PICK_TARGET = 'На какой язык переводим?'

TRANSLATION_PROMPT = emojize(':telescope: Варианты перевода слова ')

USAGE_EXAMPLES_PROMPT = emojize(':telescope: Варианты использования:\n')

LANGUAGES = {
    'ru': emojize(':Russia: Русский'),
    'en': emojize(':United_Kingdom: Английский'),
    'de': emojize(':Germany: Немецкий'),
    'es': emojize(':Spain: Испанский'),
    'fr': emojize(':France: Французский'),
    'it': emojize(':Italy: Итальянский'),
    'pt': emojize(':Portugal: Португальский'),
    'tr': emojize(':Turkey: Турецкий')
}

LANGUAGE_EMOJIS = {
    'ru': emojize(':Russia:'),
    'en': emojize(':United_Kingdom:'),
    'de': emojize(':Germany:'),
    'es': emojize(':Spain:'),
    'fr': emojize(':France:'),
    'it': emojize(':Italy:'),
    'pt': emojize(':Portugal:'),
    'tr': emojize(':Turkey:')
}
