def scramble(s1, s2):
    newlist = []
    for i in list(s2):
        if i in  list(s1):
            newlist.append(i)
    if newlist==list(s2):
        return True
    else:
        return False


print(scramble('cubtvzhetokfsd', 'bohzsdcetvtfuk'))