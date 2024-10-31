def calculate_love_score(name1, name2):
    #rint(name1+name2)
    fullnames = list(name1+name2)
    #print(fullnames)
    equation1 = 0
    equation2 = 0
    sum = 0
    for firstLetterCheck in 'true':
        for congruency in fullnames:
            if firstLetterCheck == congruency:
                sum += 1
                equation1 += 1
        print(f"{firstLetterCheck.upper()} occurs {sum} times.")
        sum = 0
    print(f"Total = {equation1}")

    for secondLetterCheck in 'love':
        for congruency in fullnames:
            if secondLetterCheck == congruency:
                sum += 1
                equation2 += 1
        print(f"{secondLetterCheck.upper()} occurs {sum} times.")
        sum = 0
    print(f"Total = {equation2}")
    print(f"Love Score {equation1}{equation2}")

calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
