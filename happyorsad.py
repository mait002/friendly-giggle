mood = input()
happy = mood.count(':-)')
sad = mood.count(':-(')

if happy == 0 and sad == 0:
    output = 'none'
elif happy > sad:
    output = 'happy'
elif happy < sad:
    output = 'sad'
elif happy == sad:
    output = 'unsure'

print(output)

