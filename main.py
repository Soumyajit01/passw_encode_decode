import random
import string
letters = string.ascii_lowercase
characters = ['!','@','#','$','%','^','&','*','_','.']
random.shuffle(characters)
def encode(passw):
    passw=list(passw[::-1]) # reversing the sequence
    start_chars=''.join(random.choices(letters,k=3))
    end_chars=''.join(random.choices(letters,k=3))
    hashed_list = [x for pair in zip(passw, characters) for x in pair]
    mid_chars=''.join(hashed_list)
    return start_chars+mid_chars+end_chars

    
def decode(text):
    pass
