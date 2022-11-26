import telebot.types
from reverso_context_api import Client
from telegram_bot.utils import messages
from telegram_bot.utils.translations import (make_translations_list,
                                             make_usage_examples_list)


def run_bot(bot):

    lang_pair = {
        'source': 'en',
        'target': 'ru'
    }

    @bot.message_handler(commands=['start'])
    def start_command(m):
        """ Handles /start command """
        bot.send_message(m.chat.id, messages.START)

    @bot.message_handler(commands=['help'])
    def help_command(m):
        """ Handles /help command """
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                'Написать разработчику', url='t.me/alropo'
            )
        )
        bot.send_message(m.chat.id, messages.HELP, reply_markup=keyboard)

    @bot.message_handler(commands=['picklanguages'])
    def pick_languages_command(m):
        source_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
        bt_en = telebot.types.InlineKeyboardButton(messages.LANGUAGES['en'],
                                                   callback_data='source-en')
        bt_ru = telebot.types.InlineKeyboardButton(messages.LANGUAGES['ru'],
                                                   callback_data='source-ru')
        bt_de = telebot.types.InlineKeyboardButton(messages.LANGUAGES['de'],
                                                   callback_data='source-de')
        bt_es = telebot.types.InlineKeyboardButton(messages.LANGUAGES['es'],
                                                   callback_data='source-es')
        bt_fr = telebot.types.InlineKeyboardButton(messages.LANGUAGES['fr'],
                                                   callback_data='source-fr')
        bt_it = telebot.types.InlineKeyboardButton(messages.LANGUAGES['it'],
                                                   callback_data='source-it')
        bt_pt = telebot.types.InlineKeyboardButton(messages.LANGUAGES['pt'],
                                                   callback_data='source-pt')
        bt_tr = telebot.types.InlineKeyboardButton(messages.LANGUAGES['tr'],
                                                   callback_data='source-tr')
        source_keyboard.add(bt_en, bt_ru, bt_de, bt_es,
                            bt_fr, bt_it, bt_pt, bt_tr)
        bot.send_message(m.chat.id, messages.PICK_SOURCE,
                         reply_markup=source_keyboard)

    @bot.callback_query_handler(
        func=lambda callback: callback.data.startswith('source')
    )
    def get_source_language_set_up_target(callback):
        bot.answer_callback_query(callback.id)
        source = callback.data[7:]
        lang_pair['source'] = source

        target_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
        bt_en = telebot.types.InlineKeyboardButton(messages.LANGUAGES['en'],
                                                   callback_data='target-en')
        bt_ru = telebot.types.InlineKeyboardButton(messages.LANGUAGES['ru'],
                                                   callback_data='target-ru')
        bt_de = telebot.types.InlineKeyboardButton(messages.LANGUAGES['de'],
                                                   callback_data='target-de')
        bt_es = telebot.types.InlineKeyboardButton(messages.LANGUAGES['es'],
                                                   callback_data='target-es')
        bt_fr = telebot.types.InlineKeyboardButton(messages.LANGUAGES['fr'],
                                                   callback_data='target-fr')
        bt_it = telebot.types.InlineKeyboardButton(messages.LANGUAGES['it'],
                                                   callback_data='target-it')
        bt_pt = telebot.types.InlineKeyboardButton(messages.LANGUAGES['pt'],
                                                   callback_data='target-pt')
        bt_tr = telebot.types.InlineKeyboardButton(messages.LANGUAGES['tr'],
                                                   callback_data='target-tr')
        target_keyboard.add(bt_en, bt_ru, bt_de, bt_es,
                            bt_fr, bt_it, bt_pt, bt_tr)
        bot.send_message(
            callback.message.chat.id,
            f'Супер! Переводим с {messages.LANGUAGE_EMOJIS[source]}.'
        )
        bot.send_message(
            callback.message.chat.id,
            messages.PICK_TARGET, reply_markup=target_keyboard
        )

    @bot.callback_query_handler(
        func=lambda callback: callback.data.startswith('target')
    )
    def get_target_language(callback):
        bot.answer_callback_query(callback.id)
        target = callback.data[7:]
        lang_pair['target'] = target
        bot.send_message(
            callback.message.chat.id,
            f'Принято! Переводим на {messages.LANGUAGE_EMOJIS[target]}. '
            f'Теперь я готов! Присылайте мне слово или словосочетание.'
        )

    @bot.message_handler(content_types=['text'])
    def translate(m):
        """ Returns translation and usage examples for given word/phrase """

        # get translations and usage examples gens from Reverso Context API
        source_lang = lang_pair.get('source')
        target_lang = lang_pair.get('target')
        client = Client(source_lang, target_lang)
        trans_iter = client.get_translations(m.text)
        usage_examples_iter = client.get_translation_samples(m.text)
        # refactor generators into readable translations
        translations = make_translations_list(trans_iter)
        examples = make_usage_examples_list(usage_examples_iter,
                                            source_lang, target_lang)
        # put together reply message
        translation_message = f'*{messages.TRANSLATION_PROMPT}"' \
                              f'{m.text}":*\n\n' \
                              f'{translations}\n\n' \
                              f'*{messages.USAGE_EXAMPLES_PROMPT}*\n' \
                              f'{examples}'

        bot.send_message(m.chat.id, translation_message)
