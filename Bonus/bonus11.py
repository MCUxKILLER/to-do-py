feet_inches = input("Enter feet and inches : ")


def convert(feet_inches):
    hold = list(map(float, feet_inches.split()))
    feet = hold[0]
    inches = hold[1]
    return feet * 0.3048 + inches * 0.0254


print(convert(feet_inches))

