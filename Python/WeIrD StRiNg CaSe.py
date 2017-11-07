def to_weird_case(string):
    ans = []
    string = string.split()
    for j in string:
        i = 0
        temp = ''
        while i < len(j):
            if i % 2 == 0:
                temp += j[i].upper()
            else:
                temp += j[i].lower()
            i += 1
        ans.append(temp)
    return ' '.join(ans)

print(to_weird_case('my name is rooha'))