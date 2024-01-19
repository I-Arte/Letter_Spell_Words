# Code purpose: convert words to a series of letters that when spelled, will sound like the original word in english. i.e: deity = d a t

import transAFI
import eng_to_ipa

diclave = {"a":["a"],"b":["be"],"c":["se","ce","ze"],"d":["de"],"e":["e"],"f":["efe"],"g":["ge","je"],"h":["ache"],"i":["i"],"j":["jota"],"k":["ca","ka"],
"l":["ele"],"m":["eme"], "n":["ene"], "ñ":["enie","eñe"], "o":["o"], "p":["pe"], "q":["cu","que"],"r":["erre","ere"],"s":["ese","ece","eze"],"t":["te"],"u":["u"],
"v":["ve"], "w":["w"],"x":["equis"], "y":["ye"], "z":["ceta"],"":[" "], "":["h"]}

#diclave_AFI = {k:[str(eng_to_ipa.convert(s)).replace("ˌ","").replace("ˈ","").replace("*","") for s in v] for k,v in diclave.items()}

diclave_AFI = {k:v for k in diclave.keys() for v in eng_to_ipa.ipa_list((str(k)).upper()) }

diclave_AFI.update({'0': ['ˈziroʊ'], '1': ['wən',"hwən"], '2': ['tu'], '3': ['θri'], '4': ['fɔr'], '5': ['faɪv'], '6': ['sɪks'], '7': ['ˈsɛvən'], '8': ['eɪt'], '9': ['naɪn'], '10': ['tɛn'], '11': ['ɪˈlɛvən', 'ˈilɛvən'], '12': ['twɛlv'], '13': ['ˈθərˈtin'], '100': ['ˈhəndrəd', 'ˈhəndrɪd', 'ˈhəndərd', 'ˈhənərd']})

def checker(word, dict, i):
    possible = []
    for key, values in dict.items():
        for value in values:
            if word[i:i + len(value)] == value:
                possible.append((key, value))
    if len(possible)> 0:
        longest_match = max(possible, key=lambda x: len(x[1]))
    else:
        longest_match = None
    if longest_match != None and len(longest_match[1])>0:
        return longest_match

def conversor(*words):
    word = ''
    for i in words:
        i = str(i).replace(" ","")
        word += i
    word_list = eng_to_ipa.ipa_list(word)
    new_word = ""
    global diclave_AFI
    #new_dict = {key: [s[::-1] for s in value] for key, value in diclave.items()}
    for W in word_list:
        i = 0
        for w in W:
            w=w.replace("ˌ", "").replace("ˈ", "").replace("*", "")
            while i < len(w):
                match = checker(w,diclave_AFI,i)
                match2 = checker(w,diclave_AFI,i-1)
                if match != None:
                    new_word += match[0]
                    i += len(match[1])
                elif match2 and len(match2[1])>1:
                    new_word += match2[0]
                    i += len(match2[1])-1
                else:
                    new_word = ''
                    i=0
                    break
        if new_word != '' and new_word != word:
            return (f'{new_word} = {word}')

print(conversor("vienna"))


with open("EnglishWords.txt", "r", encoding="utf-8") as f:
    Palabras = f.read().replace('\n', ' ').split(" ")

Final_Words = []
for item in Palabras:
    Final_Words.append(item.lower())

x = list(filter(None,(map(conversor, Final_Words))))

with open("Converted_Words.txt", "w") as file:
    for item in x:
        file.write(item + '\n') 
        