filenames = ['1.Raw.txt', '2.Hero.txt', '3.Villain.txt']
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)
print(filenames)
