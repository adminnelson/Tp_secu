message_a_code=input("entrez votre texte :")
clef=int(input("rentrez votre cle:"))
message=[]
message_decode=[]
for i in message_a_code:
    message.append(ord(i)+clef)
for i in message:
    message_decode.append(chr(i))
final="".join(message_decode)
print(final)  