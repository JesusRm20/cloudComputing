import bcrypt

def hashPassword(pwd):
    password = pwd.encode('utf-8')
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())

    return hashed

def passwordCheck(pwd, hashedpwd):
    resp = bcrypt.checkpw(pwd.encode('utf-8'),hashedpwd.encode('utf-8'))
    if resp:
        return True
    else:
        return False
passdb = '$2b$12$BVFGyDI9molqBOXEgHB9G.mR2v3QPjHcQHSheedyh0qYvsSeIkP6u'
pass2 = "$2b$12$BVFGyDI9molqBOXEgHB9G.mR2v3QPjHcQHSheedyh0qYvsSeIkP6u                                                                                                                                            ".strip()
pass1 = 'jesus'

print(passwordCheck(pass1, pass2))