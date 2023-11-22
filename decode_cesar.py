message_a_decode=input("entrez votre texte :")
clef=int(input("rentrez votre cle:"))
message=[]
message_code=[]
for i in message_a_decode:
    message.append(ord(i)-clef)
for i in message:
    message_code.append(chr(i))
final="".join(message_code)
print(final)  