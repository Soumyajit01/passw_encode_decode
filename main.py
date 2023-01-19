import random
import string
letters = string.ascii_lowercase

def encode(text):
    if len(text)>=3:
        start_random = random.choices(letters,k=3)
        end_random = random.choices(letters,k=3)
        text=text+text[0]
        text=text.replace(text[0],'',1)
        text=(''.join(start_random))+text+(''.join(end_random))
    elif len(text)<3:
        text=text[::-1]
    return text
def decode(text):
    if len(text)<3:
        text=text[::-1]
    else:
        text=text[3:-3]
        text=(text[len(text)-1]+text)[:-1]
    return text
