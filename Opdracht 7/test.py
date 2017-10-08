def cities():
    '''returns the list of cities that are interactively entered by the user; the empty string ends the interactive input'''
    lst = []

    city = input('Enter city: ')                    # ask user to enter first city

    while city != '':                               # if city is not the flag value
        lst.append(city)                            # append city to list
        city = input('Enter city: ')                # and ask user once again

        return lst

cities()