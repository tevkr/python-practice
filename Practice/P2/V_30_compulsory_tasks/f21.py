def f21(x):
    if x[0] == 1999:
        if x[2] == 1991:
            if x[1] == 'cson':
                return 0
            elif x[1] == 'muf':
                return 1
            elif x[1] == 'pike':
                return 2
            else:
                return None
        elif x[2] == 1998:
            if x[1] == 'cson':
                return 3
            elif x[1] == 'muf':
                return 4
            elif x[1] == 'pike':
                return 5
            else:
                return None
        else:
            return None
    elif x[0] == 1977:
        if x[1] == 'cson':
            return 6
        elif x[1] == 'muf':
            if x[2] == 1991:
                return 7
            elif x[2] == 1998:
                return 8
            else:
                return None
        elif x[1] == 'pike':
            return 9
        else:
            return None
    else:
        return None