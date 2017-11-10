def newPassword():

    oldpassword = 'QwErTy123'
    newpassword = input('voer nieuwe wachtwoord in')

    while True:

        if newpassword == oldpassword:
            print('je wachtwoord mag niet hetzelfde zijn!')
            newpassword = input('voer nieuwe wachtwoord in')

        if len(newpassword) <= 5:
            print('je wachtwoord moet minimaal 6 karakters bevatten!')
            newpassword = input('voer nieuwe wachtwoord in')

        else:
            print('Je wachtwoord is succesvol veranderd.')
            print(newpassword)
            return True

newPassword()