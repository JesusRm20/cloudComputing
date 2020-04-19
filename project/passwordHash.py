import bcrypt

def hashPassword(pwd):
    password = pwd.encode('utf-8')
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())

    return hashed

def passwordCheck(pwd, hashedpwd):
    pwd = pwd.encode('utf-8')
    resp = bcrypt.checkpw(pwd,hashedpwd)
    if resp:
        return True
    else:
        return False

