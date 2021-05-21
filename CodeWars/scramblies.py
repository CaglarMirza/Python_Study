def scramble(s1, s2):
    return all([True if s2.count(i)<=s1.count(i) else False for i in s2])


    ###########-----------------




def scramble(s1, s2):
    newlist = []
    denem = list(s1)
    for i in list(s2):
        if i in  denem:
            newlist.append(i)
            denem.remove(i)
    if newlist==list(s2):
        return True
    else:
        return False


print(scramble('', ''))