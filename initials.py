
def get_initials(fullname):
    """ Given a person's name, return the person's initials (upper) """
    name = fullname.split()
    initials = ''

    for x in name:
        initials = initials + x[0]

    answer = initials.upper()
    return (answer)

#name = input('What is your name?')
#print(get_initials(name))

#print(get_initials('Ozzie Smith'))
#print(get_initials('Wanda Nicole Evans'))
#print(get_initials('  Adam Hotaling   '))
