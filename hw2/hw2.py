#3:Спрашивает у пользователя слово и выводит на экран все буквы этого слова задом наперёд, пропуская буквы "з" и "я".

st=input()
new_st=""
for i in range(len(st)):
    for letter in st:
        if letter != "з" and letter != "я":
            new_st += letter
    break
print(new_st[::-1])
