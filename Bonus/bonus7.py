date = input("Enter today's date: ")
rate = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n").capitalize()

filename = f"..\\journal\\{date}.txt"
with open(filename, "w") as file:
    file.write(f"{rate}\n\n")
    file.write(f"{thoughts}\n")
