
text= input('Enter your text:')
result=""
for i in range(len(text)):
    if text[i].lower() =='c':
        result+=str(i) + "-"
print(result[:-1])



