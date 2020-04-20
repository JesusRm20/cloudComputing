import bcrypt

def hashPassword(pwd):
    password = pwd.encode('utf-8')
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())

    return hashed.encode('utf-8')

def passwordCheck(pwd, hashedpwd):
    resp = bcrypt.checkpw(pwd.encode('utf-8'),hashedpwd.encode('utf-8'))
    if resp:
        return True
    else:
        return False

