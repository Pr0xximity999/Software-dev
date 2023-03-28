from string import ascii_lowercase, ascii_uppercase

def checkPass(password):
    if len(password) != 24:
        return False

    special_pos = []
    upper_count = lower_count = special_count = number_count = 0
    
    for i, l in enumerate(password):
        if l in ascii_uppercase:
            upper_count += 1
        elif l in ascii_lowercase:
            lower_count += 1
        elif l in "@#$%&_?":
            if i == 0 or i == len(password) -1:
                return False
            special_pos.append(i)
            special_count += 1
        elif l in "1234567890":
            if i < 3:
                return False
            number_count += 1
    
    if upper_count < 2 or upper_count > 6 or lower_count < 8 or special_count != 3 or number_count < 4 or number_count > 7:
        return False

    return True, special_pos
words = ['xjuTxNCy$H6wv9#n7K442%5o', 'bnoGFa8@p1z7poivn?Ung7%m', 'Rkcoy?yBNU5tkcr5d5%6J%zu', 'kfe0$s02Uj04Bd5Q?ig$3uis', 'tng5?8m9Ku7MIO8kYj@wy$d9', 'tOk7#h27s%74xpz0qF#gP9lf']

special_pos = {}
for word in words:
    result = checkPass(word)
    if result:
        for pos in result[1]:
            if pos in special_pos:
                special_pos[pos] += 1
            else:
                special_pos[pos] = 1
        print("valid")
    else:
        print("invalid")

print(special_pos)
