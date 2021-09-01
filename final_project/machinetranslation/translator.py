"""translator instance"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ[apikey]
url = os.environ[url]

'''Access to Translator service'''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-04-21',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def en_fr(en_txt):
    """English to french translator function"""
    fr_translation=language_translator.translate(
    text=(en_txt),
    model_id='en-fr').get_result()
    frenchtext=json.dumps(fr_translation['translations'][0]['translation'],
    indent=2, ensure_ascii=False)
    return frenchtext

def fr_en(fr_txt):
    """french to english translator function"""
    en_translation=language_translator.translate(
    text=(fr_txt),
    model_id='fr-en').get_result()
    englishtext=json.dumps(en_translation['translations'][0]['translation'],
    indent=2, ensure_ascii=False)
    return englishtext
    