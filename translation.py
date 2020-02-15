from drivingtest.models import *

from modeltranslation.translator import translator, TranslationOptions


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question',)
    required_languages = ('hi',)

class OptionTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('hi',)

translator.register(Question, QuestionTranslationOptions)
translator.register(Option, OptionTranslationOptions)
