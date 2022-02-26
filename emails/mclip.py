import pyperclip
import sys

TEXT = {
    'new': '''
    Hi,
    Thank you for contacting me.
    I'm looking into this and will update you as soon as I have more information.
    Thank you,
    Daniela''',
    'vac': '''
    Hi,
    I'm currently away on vacations. I will get back to you as soon as I come back.
    Thank you,
    Daniela
    '''  
}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase ntext')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)
