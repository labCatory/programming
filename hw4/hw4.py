nw3 = 0
nw1 = 0
with open("text.txt", "r", encoding="utf-8") as t:
    for line in t:
        words = line.split()
        for i in words:
            if len(i) == 3:
                nw3 += 1
            elif len(i) == 1:
                nw1 += 1;
if nw1 == 0:
    print("нет слов длины 1")
elif nw3 == 0:
    print("нет слов длины 3")
else:
    print("в тексте слов длины 3 в ", nw3 / nw1, " раз больше, чем слов длины 1")
