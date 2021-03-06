#FUNCTION OF SUM OF VOWELS
def calculateVowels(textStr,vowelBig,vowelSmall):
    countVowel = 0
    for vowel in textStr:
        if ((vowel in vowelSmall) or (vowel in vowelBig)):
            countVowel += 1
    return countVowel

#DEFINITION CONSTANTS OF LOWERCASE AND UPPERCASE VOWELS 
VOWELSMALL = "aáeéěiíoóuúůyý"
VOWELBIG = "AÁEÉĚIÍOÓUÚŮYÝ"

#INPUT
textStr = input("Input text, where you want to find wovels: ") #input string by user

#SHOW VOWELS IN SPECIFIC TEXT
newStr = ""
for letter in textStr:
    if ((letter in VOWELSMALL) or (letter in VOWELBIG)): #registration of vowels with brackets 
        newStr += "(%s)" %letter
    else:   #registration of other letters
        newStr += letter 

#OUTPUT

if len(textStr) != 0:
    print(f"\nV You can find {calculateVowels(textStr,VOWELBIG,VOWELSMALL)} vowels in the text.")
    print("See vowels:\n",newStr,"\n")
else:
    print("You inputed empty string!!")