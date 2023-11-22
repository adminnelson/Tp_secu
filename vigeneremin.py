def Vigenere(c,cle):
    indice_cle=0
    msg_code=""
    
    for i in range(0,len(c)):
        if 'a'<=c[i]<='z':
            msg_code+=chr((((ord(c[i])-ord('A'))+(ord(cle[indice_cle])-ord('A')))% 26)+ord('A'))
            indice_cle=(indice_cle +1)%len(cle)
        else:
            msg_code+=c[i]
    return msg_code

def Deco_vigenere(c,cle):
    indice_cle=0
    msg_code=""
    
    for i in range(0,len(c)):
        if 'a'<=c[i]<='z':
            msg_code+=chr((((ord(c[i])-ord('A'))-(ord(cle[indice_cle])-ord('A')))% 26)+ord('A'))
            indice_cle=(indice_cle +1)%len(cle)
        else:
            msg_code+=c[i]
    return msg_code

print(Vigenere('BONJOUR A TOUS','python'))
print(Deco_vigenere('QMGQCHG Y MVIF','PYTHON'))