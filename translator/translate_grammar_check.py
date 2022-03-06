from googletrans import Translator
from gingerit.gingerit import GingerIt


def grammar_spelling_check(text):
    parser = GingerIt()
    b = parser.parse(text)['result'] 
    return b


def translating(text, language):
    translator = Translator()
    translate = translator.translate(text, dest= language)
    return translate.text

