from google.cloud import translate

def translator(text, language):
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language=language)
    return translation['translatedText']