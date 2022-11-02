koef = 1.7777777777777777
startW = 1920
startH = 1080
print(startW/startH)
for w in range(1, 1921):
    for h in range(1, 1081):
        if (w / h) == koef:
            print(w)
            print(h)
