from ast import Str
from errno import ENFILE
from unittest import result
import unittest

unitdict={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "":0}
tendict={"ten":0, "eleven":1,"twelve":2, "thirteen":3, "fourteen":4, "fifteen":5, "sixteen":6, "seventeen":7, "eighteen":8, "nineteen":9} # the ten digit will always be 1
tydict={"twenty":2, "thirty":3, "forty":4, "fifty":5, "sixty":6, "seventy":7, "eighty":8, "ninety":9}
bigdict=["hundred", "thousand", "million", "billion", "trillion"]
goodword=bigdict.copy()
for unit in unitdict.keys(): goodword.append(unit)
for ten in tendict.keys(): goodword.append(ten)
for ty in tydict.keys(): goodword.append(ty)

def EnglishToInteger(englishNumber: Str) -> int:
    def ValueErrorRaiser():
        raise ValueError("We can't accept this number, put in a valid one")

    def digitPlacer(numlistd, engNumd, wordlistd, largenumber, engNumLength):
        #print(numlistd,engNumd,wordlistd,largenumber,engNumLength)
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
        try:
            if wordlistd[0] in bigdict:
                    ValueErrorRaiser() 
            if wordlistd[1] == "hundred":
                if wordlist[0] not in unitdict:
                    ValueErrorRaiser()
                numlistd[0+unitmove]=unitdict[wordlistd[0]]
            #if something hundred and ... 
                if wordlistd[2] in tydict:
                    numlistd[1+unitmove]=tydict[wordlistd[2]]
                    if wordlistd[3] in unitdict:
                        numlistd[2+unitmove]=unitdict[wordlistd[3]]
                    elif wordlistd[3] in tydict or wordlistd in tendict:
                        ValueErrorRaiser()
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
                    if wordlistd[1] in unitdict or wordlistd[1] in tendict or wordlistd[1] in tydict or wordlistd[1] == "hundred":
                        ValueErrorRaiser()
                    numlistd[1+unitmove]=1
                    numlistd[2+unitmove]=tendict[wordlistd[0]]
                elif wordlistd[0] in unitdict:
                    if wordlistd[1] in unitdict or wordlistd[1] in tendict or wordlistd[1] in tydict:
                        ValueErrorRaiser()
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
        except IndexError:
            ValueErrorRaiser()
    if not type(englishNumber) is str or englishNumber.isnumeric() or englishNumber == "and" or englishNumber == "" or englishNumber.isspace():
        ValueErrorRaiser()
    wordlist=englishNumber.replace(',',"").lower().replace(' and', "").replace('-', " ").split()
    for word in wordlist:
        if not word in goodword:
            ValueErrorRaiser()
    numlist= [0] * 15
    if wordlist.count("thousand") > 1 or wordlist.count("million") > 1 or wordlist.count("billion") > 1 or wordlist.count("trillion") > 1:
        ValueErrorRaiser()
    #trillion segment
    k=len(wordlist)
    if "trillion" in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "trillion", k)
        goodword.remove("trillion")

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
    if 'thousand' in englishNumber:
        digitPlacer(numlist, englishNumber, wordlist, "thousand", k)

    #hundreds segment
    k=len(wordlist)
    if k > 4:
        ValueErrorRaiser()
    if "hundred" in wordlist:
        if wordlist[0] not in unitdict:
            ValueErrorRaiser()
        numlist[12]=unitdict[wordlist[0]]
        if k == 4: #if the numlist is in 4 words: [hundred number], ['hundred'], [ty number], [unit number]
            if wordlist[2] in tydict:
                numlist[13]=tydict[wordlist[2]]
                numlist[14]=unitdict[wordlist[3]]
            elif wordlist[2] not in tydict and wordlist[3] in goodword:
                ValueErrorRaiser()
        elif k == 3: # if numlist is [hundred number], hundred, [unit number/ ty number/ ten number]
            if wordlist[2] in tydict:
                numlist[13]=tydict[wordlist[2]]
            elif wordlist[2] in tendict:
                numlist[13]=1
                numlist[14]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[14]=unitdict[wordlist[2]]
    elif k == 2: #if numlist is [ty number], [unit number]
        if wordlist[0] in tydict:
            numlist[13]=tydict[wordlist[0]]
            numlist[14]=unitdict[wordlist[1]]
        else:
            ValueErrorRaiser()
    elif k == 1:
        if wordlist[0] in tydict:
            numlist[13]=tydict[wordlist[0]]
        if wordlist[0] in tendict:
            numlist[13]=1
            numlist[14]=tendict[wordlist[0]]
        if wordlist[0] in unitdict:
            numlist[14]=unitdict[wordlist[0]]

    while True:
        try:
            if numlist[0] == 0:
                numlist.pop(0)
            else:
                break
        except IndexError:
            ValueErrorRaiser()
    resultnumber=int("".join(map(str,numlist)), base=10)
    print(resultnumber)
    return resultnumber

EnglishToInteger("fourteen trillion, sixty-four thousand")
EnglishToInteger("seven billion")

EnglishToInteger("one")
EnglishToInteger("ten")
EnglishToInteger("fifty")
EnglishToInteger("sixty-two")
EnglishToInteger("six hundred")
EnglishToInteger("six hundred and two")
EnglishToInteger("six hundred and twelve")
EnglishToInteger("six hundred and fifty")
EnglishToInteger("six hundred and fifty-four")
EnglishToInteger("one thousand")
EnglishToInteger("one thousand and one")
EnglishToInteger("one thousand and sixteen")
EnglishToInteger("one thousand and sixty")
EnglishToInteger("one thousand and sixty-three")
EnglishToInteger("one thousand, two hundred")
EnglishToInteger("one thousand two hundred and one")
EnglishToInteger("one thousand two hundred and thirteen")
EnglishToInteger("one thousand two hundred and thirty")
EnglishToInteger("one thousand two hundred and thirty-four")
EnglishToInteger("ten thousand")
EnglishToInteger("eleven thousand and one")
EnglishToInteger("eleven thousand and sixteen")
EnglishToInteger("ten thousand and sixty")
EnglishToInteger("ten thousand and sixty-three")
EnglishToInteger("ten thousand, two hundred")
EnglishToInteger("ten thousand two hundred and one")
EnglishToInteger("ten thousand two hundred and thirteen")
EnglishToInteger("ten thousand two hundred and thirty")
EnglishToInteger("ten thousand two hundred and thirty-four")
EnglishToInteger("fifty thousand")
EnglishToInteger("fifty thousand and one")
EnglishToInteger("fifty thousand and sixteen")
EnglishToInteger("fifty thousand and sixty")
EnglishToInteger("fifty thousand and sixty-three")
EnglishToInteger("fifty thousand, two hundred")
EnglishToInteger("fifty thousand two hundred and one")
EnglishToInteger("fifty thousand two hundred and thirteen")
EnglishToInteger("fifty thousand two hundred and thirty")
EnglishToInteger("thirty thousand two hundred and thirty-four")

EnglishToInteger("fifty-one thousand")
EnglishToInteger("fifty-one thousand and one")
EnglishToInteger("fifty-one thousand and sixteen")
EnglishToInteger("fifty-one thousand and sixty")
EnglishToInteger("fifty-one thousand and sixty-three")
EnglishToInteger("fifty-one thousand, two hundred")
EnglishToInteger("fifty-one thousand two hundred and one")
EnglishToInteger("fifty-one thousand two hundred and thirteen")
EnglishToInteger("fifty-one thousand two hundred and thirty")
EnglishToInteger("thirty-one thousand two hundred and thirty-four")

EnglishToInteger("eight hundred thousand")
EnglishToInteger("eight hundred thousand and one")
EnglishToInteger("eight hundred thousand and sixteen")
EnglishToInteger("eight hundred thousand and sixty")
EnglishToInteger("eight hundred thousand and sixty-three")
EnglishToInteger("eight hundred thousand, two hundred")
EnglishToInteger("eight hundred thousand two hundred and one")
EnglishToInteger("eight hundred thousand two hundred and thirteen")
EnglishToInteger("eight hundred thousand two hundred and thirty")
EnglishToInteger("eight hundred thousand two hundred and thirty-four")

assert EnglishToInteger("one twenty-forty") == ValueError
