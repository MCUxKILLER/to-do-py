contents = ['jump',
            'out',
            'the window']
filenames = ['doc.txt', 'out.txt', 'place.txt']

for content, filename in zip(contents, filenames):
    filepath = "..\\Coding_exercise\\" + filename
    with open(filepath, 'w') as file:
        file.write(content)
