from ast import Str
from errno import ENFILE
from unittest import result

unitdict={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "":0}
tendict={"ten":0, "eleven":1,"twelve":2, "thirteen":3, "fourteen":4, "fifteen":5, "sixteen":6, "seventeen":7, "eighteen":8, "nineteen":9} # the ten digit will always be 1
tydict={"twenty":2, "thirty":3, "forty":4, "fifty":5, "sixty":6, "seventy":7, "eighty":8, "ninety":9}
goodword=["hundred", "thousand", "million", "billion", "trillion"]
for unit in unitdict.keys():
    goodword.append(unit)
for ten in tendict.keys():
    goodword.append(ten)
for ty in tydict.keys():
    goodword.append(ty)


def EnglishToInteger(englishNumber: Str) -> int:
    if not type(englishNumber) is str or englishNumber.isnumeric() or englishNumber == "and" or englishNumber == "":
        raise ValueError("This is not a lettered number")
        return -1
    commaremoved=englishNumber.replace(',',"")
    andremoved=commaremoved.replace(' and', "")
    dashremoved=andremoved.replace('-', " ")
    wordlist=dashremoved.split()
    print(wordlist)
    for word in wordlist:
        if not word in goodword:
            raise ValueError("We can't accept this number")
            return -1
    numlist= [0] * 15

    #trillion segment
    k=len(wordlist)
    if "trillion" in englishNumber:
        if englishNumber == "trillion":
            raise ValueError("We can't accept this number")
            return -1
        if wordlist[1] == "hundred":
            numlist[0]=unitdict[wordlist[0]] #
        if k == 2:   #if the word is 2 words long (either 1-19 or [number]0 trillion)
            if wordlist[0] in tydict:
                numlist[1]=tydict[wordlist[0]]
            if wordlist[0] in tendict:
                numlist[1]=1
                numlist[2]=tendict[wordlist[0]]
            if wordlist[0] in unitdict:
                numlist[2]=unitdict[wordlist[0]]
        else:
            if wordlist[2] in tydict:
                numlist[1]=tydict[wordlist[2]]
                if wordlist[3] in unitdict:
                    numlist[2]=unitdict[wordlist[3]]
            elif wordlist[2] in tendict:
                numlist[1]=1
                numlist[2]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[2]=unitdict[wordlist[2]]
            if wordlist[0] in tydict:
                numlist[1]=tydict[wordlist[0]]
                if wordlist[1] in unitdict:
                    numlist[2]=unitdict[wordlist[1]]
            elif wordlist[0] in tendict:
                numlist[1]=1
                numlist[2]=tendict[wordlist[0]]
            if wordlist[0] in unitdict and not wordlist[1] == "hundred":
                numlist[2]=unitdict[wordlist[0]]
        
        while True:
            if wordlist[0]== "trillion":
                wordlist.pop(0)
                break
            wordlist.pop(0)
            
    #billions segment
    k=len(wordlist)        
    if "billion" in englishNumber:
        if englishNumber == "billion":
            raise ValueError("We can't accept this number")
            return -1
        if wordlist[1] == "hundred":
            numlist[3]=unitdict[wordlist[0]]
        if k == 2:   #if the word is 2 words long (either 1-19 or [number]0 trillion)
            if wordlist[0] in tydict:
                numlist[4]=tydict[wordlist[0]]
            if wordlist[0] in tendict:
                numlist[4]=1
                numlist[5]=tendict[wordlist[0]]
            if wordlist[0] in unitdict:
                numlist[5]=unitdict[wordlist[0]]
        else:
            if wordlist[2] in tydict:
                numlist[4]=tydict[wordlist[2]]
                if wordlist[3] in unitdict:
                    numlist[5]=unitdict[wordlist[3]]
            elif wordlist[2] in tendict:
                numlist[4]=1
                numlist[5]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[5]=unitdict[wordlist[2]]
            if wordlist[0] in tydict:
                numlist[4]=tydict[wordlist[0]]
                if wordlist[1] in unitdict:
                    numlist[5]=unitdict[wordlist[1]]
            elif wordlist[0] in tendict:
                numlist[4]=1
                numlist[5]=tendict[wordlist[0]]
            if wordlist[0] in unitdict and not wordlist[1] == "hundred":
                numlist[5]=unitdict[wordlist[0]]

        while True:
            if wordlist[0]== "billion":
                wordlist.pop(0)
                break
            wordlist.pop(0)

    #millions segment
    k=len(wordlist)
    if "million" in englishNumber:
        if englishNumber == "million":
            raise ValueError("We can't accept this number")
            return -1
        if wordlist[1] == "hundred":
            numlist[6]=unitdict[wordlist[0]] #
        if k == 2:   #if the word is 2 words long (either 1-19 or [number]0 trillion)
            if wordlist[0] in tydict:
                numlist[7]=tydict[wordlist[0]]
            if wordlist[0] in tendict:
                numlist[7]=1
                numlist[8]=tendict[wordlist[0]]
            if wordlist[0] in unitdict:
                numlist[8]=unitdict[wordlist[0]]
        else:
            if wordlist[2] in tydict:
                numlist[7]=tydict[wordlist[2]]
                if wordlist[3] in unitdict:
                    numlist[8]=unitdict[wordlist[3]]
            elif wordlist[2] in tendict:
                numlist[7]=1
                numlist[8]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[8]=unitdict[wordlist[2]]
            if wordlist[0] in tydict:
                numlist[7]=tydict[wordlist[0]]
                if wordlist[1] in unitdict:
                    numlist[8]=unitdict[wordlist[1]]
            elif wordlist[0] in tendict:
                numlist[7]=1
                numlist[8]=tendict[wordlist[0]]
            if wordlist[0] in unitdict and not wordlist[1] == "hundred":
                numlist[8]=unitdict[wordlist[0]]

        while True:
            if wordlist[0]== "million":
                wordlist.pop(0)
                break
            wordlist.pop(0)

    #thousands segment
    k=len(wordlist)
    if "thousand" in englishNumber:
        if englishNumber == "thousand":
            raise ValueError("We can't accept this number")
            return -1
        if wordlist[1] == "hundred":
            numlist[9]=unitdict[wordlist[0]]
        if k == 2:
            if wordlist[0] in tydict:
                numlist[10]=tydict[wordlist[0]]
            if wordlist[0] in tendict:
                numlist[10]=1
                numlist[11]=tendict[wordlist[0]]
            if wordlist[0] in unitdict:
                numlist[11]=unitdict[wordlist[0]]
        else:
            if wordlist[2] in tydict:
                numlist[10]=tydict[wordlist[2]]
                if wordlist[3] in unitdict:
                    numlist[11]=unitdict[wordlist[3]]
            elif wordlist[2] in tendict:
                numlist[10]=1
                numlist[11]=tendict[wordlist[2]]
            elif wordlist[2] in unitdict:
                numlist[11]=unitdict[wordlist[2]]
            if wordlist[0] in tydict:
                numlist[10]=tydict[wordlist[0]]
                if wordlist[1] in unitdict:
                    numlist[11]=unitdict[wordlist[1]]
            elif wordlist[0] in tendict:
                numlist[10]=1
                numlist[11]=tendict[wordlist[0]]
            if wordlist[0] in unitdict and not wordlist[1] == "hundred":
                numlist[11]=unitdict[wordlist[0]]

        while True:
            if wordlist[0]== "thousand":
                wordlist.pop(0)
                break
            wordlist.pop(0)

    #hundreds segment
    k=len(wordlist)
    if "hundred" in wordlist:
        if englishNumber == "hundred":
            raise ValueError("We can't accept this number")
            return -1
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
        
    resultnumber=int()
    resultnumber="".join(map(str,numlist))
    resultnumber=int(resultnumber, base=10)
    print(resultnumber)
    return resultnumber

EnglishToInteger("four")
EnglishToInteger("two hundred trillion and seventy-two")
EnglishToInteger("twenty trillion")
EnglishToInteger("twenty billion")
EnglishToInteger("twenty million")
EnglishToInteger("two hundred and twenty thousand, seven hundred and forty-five")
EnglishToInteger("eleven trillion")
EnglishToInteger("eleven billion")
EnglishToInteger("eleven million")
EnglishToInteger("eleven thousand")
EnglishToInteger("six trillion")
EnglishToInteger("six billion")
EnglishToInteger("six million")
EnglishToInteger("six thousand")
EnglishToInteger("two thous")
