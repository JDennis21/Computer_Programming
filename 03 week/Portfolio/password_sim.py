while True:
    pass1 = input('Choose a password to secure your account.\n')
    pass2 = input('Verify password.\n')
    if pass1 != pass2:
        print('Passwords do not match, Try again')
    else:
        print('Password has been set.')
        break
