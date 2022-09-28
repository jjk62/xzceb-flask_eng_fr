""" Translation tool """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def connect_2_translator():
    """ connects to Watson translation service """

    load_dotenv()

    apikey = os.environ['apikey']
    url = os.environ['url']

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3( version='2018-05-01', authenticator=authenticator)
    language_translator.set_service_url( url )
    language_translator.set_disable_ssl_verification(True)

    return language_translator

def english_to_french(english_text):
    """ translates from English to French """

    french_text = ""
    if english_text is not None and len(english_text) > 0:
        translator = connect_2_translator()
        translated = translator.translate(text=english_text, model_id='en-fr').get_result()
        for line in translated["translations"] :
            french_text = french_text + line["translation"] + " "

    return french_text.rstrip()

def french_to_english(french_text):
    """ translates from French to English """

    english_text = ""
    if french_text is not None and len(french_text) > 0:
        translator = connect_2_translator()
        translated = translator.translate(text=french_text, model_id='fr-en').get_result()
        for line in translated["translations"] :
            english_text = english_text + line["translation"] + " "
        english_text = english_text.rstrip()

    return english_text.rstrip()

tr = french_to_english(None)
print(tr)
