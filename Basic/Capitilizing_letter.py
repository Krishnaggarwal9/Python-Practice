stt = input("Enter your word in lowercase: ")
uppeer = stt[0].upper()
for i in range(1,len(stt)):
    if(stt[i-1]==' '):
        uppeer+=stt[i].upper()
    else:
        uppeer+=stt[i].lower()
print("Your given word: ",uppeer)