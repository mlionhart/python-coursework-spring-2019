type = []
question1 = input("Are you more(select a or b):\t a)Thoughtful and Reserved\t  b)Active and Talkative:\t")
question2 = input("Are you more(select a or b):\t a)Concrete and Literal \t  b)Abstract and Metaphorical:\t")
question3 = input("Are you more(select a or b):\t a)Objective and Hard-nosed\t  b)Warm-hearted and Value-oriented:\t")
question4 = input("Are you more(select a or b):\t a)Orderly and Scheduled\t  b)Laid back and Resourceful:\t")

if question1 == 'a':
    type.append('I')
elif question1 == 'b':
    type.append('E')

if question2 == 'a':
    type.append('S')
elif question2 == 'b':
    type.append('N')

if question3 == 'a':
    type.append('T')
elif question3 == 'b':
    type.append('F')

if question4 == 'a':
    type.append('J')
elif question4 == 'b':
    type.append('P')

print("Your personality type is:  ", ''.join(type))
