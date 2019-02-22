#Caesar's cipher

wor = 'hello go away'#text
k = 2#key

def Encrypt(textx):
    Entextx = ''
    for i in textx:
        if i == ' ':
            Entextx = Entextx + i
        else :
            i = chr((ord(i)-97+k)%26+97)
            Entextx = Entextx + i
    return Entextx

Enc_text = Encrypt(wor)

print(Enc_text)

def Decrypt(textx):
    Entextx = ''
    for i in textx:
        if i == ' ':
            Entextx = Entextx + i
        else :
            i = chr((ord(i)-97-k)%26+97)
            Entextx = Entextx + i
    return Entextx

Dec_text = Decrypt(Enc_text)

print(Dec_text)

#print(chr((ord('o')-97+8+26)%26 + 97))
