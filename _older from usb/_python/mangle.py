from random import choice, seed
from google.cloud import translate

credentials_file = 'Proton Launcher-391ee267082a.json'
translate_client = translate.Client.from_service_account_json(credentials_file)
unformatted_languages = translate_client.get_languages()
languages = [language['language'] for language in unformatted_languages]
names = [language['name'] for language in unformatted_languages]
    
def translate_random(text, target)):
    if target == '':
        target = choice(languages)
    
    un_foreign = translate_client.translate(text, target_language=target)
    foreign = un_foreign['translatedText']

    un_translation = translate_client.translate(foreign, target_language='en')
    translation = un_translation['translatedText']
    return translation

while True:
    text = input('Text to mangle? \n')
    mode = input('Mode? \n')
    seed = input('Seed? \n')
    if seed != '':
        seed(seed)
    language = input('Language? \n')
    if language != '':
        language = languages[names.index(language)]
    
    if mode == 'print':
        while True:
            if input() != '':
                break
            else:
                text = translate_random(text)
                print(text)
                
    if mode == 'set':
        repeats = int(input('Repeats? \n'))
        for i in range(repeats):
            text = translate_random(text)
        print(text)
        
    else:
        print('Invalid mode code.')
