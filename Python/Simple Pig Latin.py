def pig_it(text):
    text_arr = text.split(' ')
    ans = []
    for i in text_arr:
        if i[:-2] + i[:-1] != 'ay' and i[0].isalpha():
            temp = i[1:] + i[0] + 'ay'
            ans.append(temp)
        else:
            ans.append(i)
    return ' '.join(ans)
