#VSTUP
textStr = input("Zadej text, u kterého chceš vybrat samohlásky: ") #zadání textu uživatelem

#DEFINICE KONSTANT MALÝCH A VELKÝCH SAMOHLÁSEK
VOWELSMALL = "aáeéěiíoóuúůyý"
VOWELBIG = "AÁEÉĚIÍOÓUÚŮYÝ"

#POČÍTADLO SAMOHLÁSEK
countVowel = 0
for vowel in textStr:
    if ((vowel in VOWELSMALL) or (vowel in VOWELBIG)):
        countVowel += 1

#VYZNAČENÍ SAMOHLÁSEK V TEXTU
newStr = ""
for letter in textStr:
    if ((letter in VOWELSMALL) or (letter in VOWELBIG)): #výpis znaku (samohlásky) se závorkou
        newStr += "(%s)" %letter
    else:   #výpis ostatních znaků
        newStr += letter 

#VÝSTUP
print(f"\nV textu je {countVowel} samohlásek")
print("Podívej se na samohlásky:\n",newStr,"\n")