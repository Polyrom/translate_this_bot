import telebot.types
from reverso_context_api import Client
from telegram_bot.utils import messages, layout
from telegram_bot.utils.translations import (make_translations_list,
                                             make_usage_examples_list)


def run_bot(bot):
    # set default language pair
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
                'Обратная связь', url=messages.FEEDBACK_URL
            )
        )
        bot.send_message(m.chat.id, messages.HELP, reply_markup=keyboard)

    @bot.message_handler(commands=['picklanguages'])
    def pick_languages_command(m):
        """ Handles /picklanguages command """
        source_keyboard = layout.make_inline_langs_keyboard('source')
        bot.send_message(m.chat.id, messages.PICK_SOURCE,
                         reply_markup=source_keyboard)

    @bot.callback_query_handler(
        func=lambda callback: callback.data.startswith('source')
    )
    def get_source_language_set_up_target(callback):
        """ Gets source language and offers to pick target language """
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.id)
        source = callback.data[7:]
        lang_pair['source'] = source
        bot.send_message(
            callback.message.chat.id,
            messages.make_lang_chosen_msg(
                messages.SOURCE_CHOSEN, source
            )
        )

        target_keyboard = layout.make_inline_langs_keyboard('target')
        bot.send_message(
            callback.message.chat.id,
            messages.PICK_TARGET, reply_markup=target_keyboard
        )

    @bot.callback_query_handler(
        func=lambda callback: callback.data.startswith('target')
    )
    def get_target_language(callback):
        """ Gets target language and finalizes language pair """
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.id)
        target = callback.data[7:]
        # check if valid language pair is given
        if lang_pair['source'] == target:
            bot.send_message(
                callback.message.chat.id,
                messages.SAME_LANGUAGES
            )
            lang_pair.update({
                'source': 'en',
                'target': 'ru'
            })
            return

        lang_pair['target'] = target

        bot.send_message(
            callback.message.chat.id,
            messages.make_lang_chosen_msg(
                messages.TARGET_CHOSEN, target
            )
        )
        bot.send_message(
            callback.message.chat.id,
            messages.READY_TO_TRANSLATE
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
