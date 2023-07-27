def validate_password(password):
    if len(password) < 8:
        return False
    else:
        res = any(x.isupper() for x in password)
        if res == False:
            return False
        else:
            res1 = any(x.islower() for x in password)
            if res1 == False:
                return False
            else:
                res2 = any(x.isdigit() for x in password)
                if res2 == False:
                    return False
                else:
                    res3 = password.find(" ") == -1
                    if res3 == False:
                        return False
                    else:
                        return True
