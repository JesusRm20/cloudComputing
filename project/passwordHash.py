import bcrypt

def hashPassword(pwd):
    password = pwd
    hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

    return hashed

def passwordCheck(pwd, hashedpwd):
    resp = bcrypt.checkpw(pwd.encode('utf-8'),hashedpwd)
    if resp:
        return True
    else:
        return False

