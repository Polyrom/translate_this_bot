from emoji import emojize

START = emojize(':woman_dancing: Можно начинать! :man_dancing: \n\n'
                'Как пользоваться ботом: /help')

HELP = emojize(':United_Kingdom: :cat: :Russia:\n'
               'По умолчанию бот переводит с английского на русский. \n\n'
               'Чтобы выбрать другую языковую пару, отправьте мне команду \n'
               '/picklanguages. \n\nЗатем напишите мне слово или '
               'простое словосочетание. Например, "Велосипед" '
               'или "Нет войне!" \n\nА я пришлю вам его перевод '
               'и примеры использования! :slightly_smiling_face:')

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

FEEDBACK_URL = 'https://t.me/FastTranslationFeedbackBot'
