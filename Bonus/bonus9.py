try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    assert width != height, "Seems to be a square"
    area = width * height

    print(area)

except AssertionError:
    print("Seems to be a square")

