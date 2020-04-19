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
passdb = '\x243262243132246a4e574f7a5a723944784d69625469514c4752755a65336c5339732e763979336e6f6b7a714e6771534448364b4e57776b676b664b'
pass1 = 'jesus'

print(passwordCheck(pass1, passdb))