import itertools
import emoji
from telegram_bot.utils.messages import LANGUAGE_EMOJIS


def make_translations_list(iterator):
    """ Returns top 5 translations in an emoji-bulleted string """
    iter_list_5 = list(itertools.islice(iterator, 5))
    emoji_list = []
    for item in iter_list_5:
        emoji_item = emoji.emojize(f':backhand_index_pointing_right:  {item}')
        emoji_list.append(emoji_item)
    return '\n'.join(emoji_list)


def make_usage_examples_list(iterator, source, target):
    """ Returns top 3 usage examples in an emoji-bulleted string """
    iter_list_3 = list(itertools.islice(iterator, 3))
    emoji_examples_list = []
    for item in iter_list_3:
        original, translation = item
        emoji_item = emoji.emojize(
            f'{LANGUAGE_EMOJIS.get(source)}  {original}\n'
            f'{LANGUAGE_EMOJIS.get(target)}  {translation}'
        )
        emoji_examples_list.append(emoji_item)
    return '\n\n'.join(emoji_examples_list)
