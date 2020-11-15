#!/usr/bin/env python3

NUMBERS = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def five_number(text):
    """A függvény kap egy számsorozatot, majd feldarabolja 5 számjegyekre. Ezek után össze szorozza ezen számokat.
    A függvény végén pedig vissza adja a legnagyobbat ezen szorzatok közül."""
    text2 = ""
    for n in text:
        if n != '\n':
            text2 = text2 + n


    number_list = []

    for i in range(len(text2)):
        number_list.append(text2[i:i+5])

    number_list2 = [int(n) for n in number_list]

    sums = []
    re_sum = 1

    for n in number_list2:
        for n_i in str(n):
            re_sum = re_sum * int(n_i)

        sums.append(re_sum)
        re_sum = 1

    """zip-et én úgy használnám, hogy tárolnám a számokat egyik értéknek a másik értéknek pedig szorzatot"""
    zipped_five_numbers = list(zip(number_list2, sums))

    return max(sums)

def main():
    print(five_number(NUMBERS))

if __name__ == "__main__":
    main()