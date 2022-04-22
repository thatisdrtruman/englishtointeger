from ast import Str
from errno import ENFILE
from unittest import result
import unittest

unitdict={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "":0}
tendict={"ten":0, "eleven":1,"twelve":2, "thirteen":3, "fourteen":4, "fifteen":5, "sixteen":6, "seventeen":7, "eighteen":8, "nineteen":9} # the ten digit will always be 1
tydict={"twenty":2, "thirty":3, "forty":4, "fifty":5, "sixty":6, "seventy":7, "eighty":8, "ninety":9}
goodword=["hundred", "thousand", "million", "billion", "trillion"]
for unit in unitdict.keys(): goodword.append(unit)
for ten in tendict.keys(): goodword.append(ten)
for ty in tydict.keys(): goodword.append(ty)

def EnglishToInteger(englishNumber: Str) -> int:
    def ValueErrorRaiser():
        raise ValueError("We can't acceipt this number, have another go")

    def digitPlacer(numlistd, engNumd, wordlistd, largenumber, engNumLength):
        if engNumd in goodword:
            ValueErrorRaiser()
        if largenumber == "trillion":
            unitmove=0
        elif largenumber == "billion":
            unitmove=3
        elif largenumber == "million":
            unitmove=6
        elif largenumber == "thousand":
            unitmove=9
        else:
            unitmove=12
        print(unitmove, wordlistd, numlistd, engNumLength)
        if wordlistd[1] == "hundred":
            numlistd[0+unitmove]=unitdict[wordlistd[0]]
            #if something hundred and ... 
            if wordlistd[2] in tydict:
                numlistd[1+unitmove]=tydict[wordlistd[2]]
                if wordlistd[3] in unitdict:
                    numlistd[2+unitmove]=unitdict[wordlistd[3]]
            elif wordlistd[2] in tendict:
                if not wordlistd[1] == largenumber:
                    numlistd[1+unitmove]=1 
                    numlistd[2+unitmove]=tendict[wordlistd[2]]
            elif wordlistd[2] in unitdict:
                if not wordlistd[1] == largenumber:
                    numlistd[2+unitmove]=unitdict[wordlistd[2]]
        if engNumLength == 2: # if english Letter number is two words long
            if wordlistd[0] in tydict:
                numlistd[1+unitmove]=tydict[wordlistd[0]]
            elif wordlistd[0] in tendict:
                numlistd[1+unitmove]=1
                numlistd[2+unitmove]=tendict[wordlistd[0]]
            elif wordlistd[0] in unitdict:
                numlistd[2+unitmove]=unitdict[wordlistd[0]]
#if zero hundred
        if wordlistd[0] in tydict:
            numlistd[1+unitmove]=tydict[wordlistd[0]]
            if wordlistd[1] in unitdict:
                numlistd[2+unitmove]=unitdict[wordlistd[1]]
        elif wordlistd[0] in tendict:
            numlistd[1+unitmove]=1
            numlistd[2+unitmove]=tendict[wordlistd[0]]
        elif wordlistd[0] in unitdict and not wordlistd[1] == "hundred":
            numlistd[2+unitmove]=unitdict[wordlistd[0]]

        while True:
            if wordlist[0]== largenumber:
                wordlist.pop(0)
                break
            wordlist.pop(0)

    if not type(englishNumber) is str or englishNumber.isnumeric() or englishNumber == "and" or englishNumber == "" or englishNumber.isspace():
        ValueErrorRaiser()
    wordlist=englishNumber.replace(',',"").lower().replace(' and', "").replace('-', " ").split()
    for word in wordlist:
        if not word in goodword:
            ValueErrorRaiser()
    numlist= [0] * 15

    #trillion segment
    k=len(wordlist)
    if "trillion" in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "trillion", k)

    #billions segment
    k=len(wordlist)        
    if "billion" in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "billion", k)

    #millions segment
    k=len(wordlist)
    if "million" in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "million", k)

    #thousands segment
    k=len(wordlist)
    if "thousand" in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "thousand", k)

    #hundreds segment
    k=len(wordlist)
    if "hundred" in wordlist:
        numlist[12]=unitdict[wordlist[0]]
        if k == 4: #if the numlist is in 4 words: [hundred number], ['hundred'], [ty number], [unit number]
            if wordlist[2] in tydict:
                numlist[13]=tydict[wordlist[2]]
                numlist[14]=unitdict[wordlist[3]]
        elif k == 3:
            if wordlist[2] in tydict:
                numlist[13]=tydict[wordlist[2]]
            elif wordlist[2] in tendict:
                numlist[13]=1
                numlist[14]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[14]=unitdict[wordlist[2]]
    elif k == 2:
        if wordlist[0] in tydict:
            numlist[13]=tydict[wordlist[0]]
            numlist[14]=unitdict[wordlist[1]]
    elif k == 1:
        if wordlist[0] in tydict:
            numlist[13]=tydict[wordlist[0]]
        if wordlist[0] in tendict:
            numlist[13]=1
            numlist[14]=tendict[wordlist[0]]
        if wordlist[0] in unitdict:
            numlist[14]=unitdict[wordlist[0]]

    while True:
        if numlist[0] == 0:
            numlist.pop(0)
        else:
            break
        
    resultnumber=int("".join(map(str,numlist)), base=10)
    print(resultnumber)
    return resultnumber



assert EnglishToInteger("Twenty thousand one hundred and twelve") == 20112
assert EnglishToInteger("Twenty-seven thousand one hundred") == 27100
assert EnglishToInteger("Twelve thousand one hundred") == 12100
assert EnglishToInteger("Three thousand one hundred") == 3100
assert EnglishToInteger("Four hundred thousand and twelve") == 400012
assert EnglishToInteger("Twenty thousand one hundred and twelve") == 20112
assert EnglishToInteger("Twenty million one hundred and twelve thousand") == 20112000
assert EnglishToInteger("Twenty million and twelve thousand") == 20012000
assert EnglishToInteger("Twenty million and twenty-five thousand") == 20025000
assert EnglishToInteger("Twenty million and five thousand") == 20005000
assert EnglishToInteger("fifteen thousand") == 15000
assert EnglishToInteger("fifty-two thousand and seven") == 52007
