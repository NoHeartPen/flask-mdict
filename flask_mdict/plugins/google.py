
# https://github.com/UlionTse/translators/tree/master
import translators as ts


def translate(content, item):
    try:
        text = ts.translate_text(
            content,
            translator='google',
            to_language=item.get('to_lan', 'zh'),
        )
        return [text]
    except ts.server.TranslatorError as err:
        return [str(err)]


def init():
    title = 'Google 翻译'
    dict_uuid = 'gtranslate'
    about = 'google-translate-for-goldendict<br />https://github.com/xinebf/google-translate-for-goldendict'
    enable = True
    config = {
        'title': title,
        'uuid': dict_uuid,
        'logo': 'google_translate.ico',
        'about': about,
        'root_path': 'translate.google.com',
        'query': translate,
        'cache': {},
        'type': 'app',
        'error': '',
        'enable': enable,
    }
    return config


if __name__ == '__main__':
    word = 'hello word'
    print('Goolge Translate', word)
    translate(word)
