oldpassword = 'QwErTy123'
newpassword = input('voer nieuwe wachtwoord in')

if newpassword == oldpassword:
    print('je wachtwoord mag niet hetzelfde zijn!')

if len(newpassword) <= 5:
    print('je wachtwoord moet minimaal 6 karakters bevatten!')

else:
    print('Je wachtwoord is succesvol veranderd.')