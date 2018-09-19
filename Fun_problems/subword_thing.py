def minion_game(string):
    # your code goes here
    print('string', string)

    # Stuart Cons
    # Kevin has to make words starting with vowels.

    vowels = 'AEIOU'

    sl = len(string)

    s_score = 0
    k_score = 0

    subwords = {}


    for start in range(sl):

        for end in range(start, sl):
            if start == end:
                continue

            substr = string[start: end]
            print(start, end, substr)
            if substr not in subwords:
                subwords[substr] = 1
            else:
                subwords[substr] += 1


    print(subwords)
    for subword in subwords:
        print(subword, subwords[subword])
        if subword[0] in vowels:
            k_score += subwords[subword]
        else:
            s_score += subwords[subword]

    if k_score == s_score:
        print("DRAW")
    elif k_score > s_score:
        print("Kevin {}".format(k_score))
    else:
        print("Stuart {}".format(s_score))

minion_game("BANANA")

string BANANA
0 1 B
0 2 BA
0 3 BAN
0 4 BANA
0 5 BANAN
1 2 A
1 3 AN
1 4 ANA
1 5 ANAN
2 3 N
2 4 NA
2 5 NAN
3 4 A
3 5 AN
4 5 N
{'BANAN': 1, 'B': 1, 'NAN': 1, 'BANA': 1, 'BA': 1, 'N': 2, 'BAN': 1, 'AN': 2, 'A': 2, 'NA': 1, 'ANA': 1, 'ANAN': 1}
BANAN 1
B 1
NAN 1
BANA 1
BA 1
N 2
BAN 1
NA 1
Stuart 9
