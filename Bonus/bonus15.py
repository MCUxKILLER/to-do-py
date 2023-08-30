import json

with open("questions.json") as file:
    content = file.read()

data = json.loads(content)
print(data)
score = 0
for question in data:
    print(question['question'])
    for j, i in enumerate(question['alternatives']):
        print(f"{j + 1}. {i}")
    try:
        prompt = int(input("Enter answer : "))
        question['user_choice'] = prompt
        if question['user_choice'] == question['correct_answer']:
            score += 1
    except ValueError:
        print("Incorrect Input")

for idx,question in enumerate(data):
    message = f"{idx+1}. Your answer : {question['user_choice']}, Correct answer: {question['correct_answer']}"
    print(message)
print(score, "/", len(data))
