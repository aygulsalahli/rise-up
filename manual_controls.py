import getch
done = False
while not done:
    char = getch.getch()
    if char == ' ':
        done = True
    else:
        char = char.lower()

    if char == 'w':
        print(char)
