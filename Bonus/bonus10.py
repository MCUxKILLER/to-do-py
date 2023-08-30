def get_averagetemp(filename):
    with open(filename) as file:
        temp = file.readlines()[1:]
    temp = list(map(float, temp))
    return sum(temp)/len(temp)


answer = get_averagetemp(r'.\files\data.txt')
print(answer)
