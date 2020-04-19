import bcrypt

def hashPassword(pwd):
    password = pwd
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())

    return hashed

def passwordCheck(pwd, hashedpwd):
    resp = bcrypt.checkpw(pwd,hashedpwd)
    if resp:
        return True
    else:
        return False

