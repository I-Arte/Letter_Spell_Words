diclave = {"a":["a"],"b":["be"],"c":["se","ce","ze"],"d":["de"],"e":["e"],"f":["efe"],"g":["ge","je"],"h":["ache"],"i":["i"],"j":["jota"],"k":["ca","ka"],
"l":["ele"],"m":["eme"], "n":["ene"], "ñ":["enie","eñe"], "o":["o"], "p":["pe"], "q":["cu"],"r":["erre","ere"],"s":["ese","ece","eze"],"t":["te"],"u":["u"],
"v":["ve"], "w":["w"],"x":["equis","por"], "y":["ye"], "z":["ceta"], "á": ["a"], "é":["e"],"í":["i"],"ó":["o"],"ú":["u"],"ü":["u"], "ï": ["i"], "ö": ["o"],  " ":[ " "],"":["h"]
           ,"0":["cero","sero"],"1":["uno"],"2":["dos"],"3":["tres","trez"],"4":["cuatro"],"5":["sicno","cinco"],"6":["seis","ceis"],"7":["ciete","siete"],"8":["ocho"],"9":["nueve"]
           ,"10":["dies","diez"],"11":["once"],"12":["doce", "dose","doze"], "13":["trece"],"100":["cien","sien"],"1000":["mil"]}

with open("PalabrasEspañol.txt", "r", encoding="utf-8") as f:
    All_Words = f.read().replace('\n', ' ').split(" ") # A list of all words to be converted.



def checker(word, dict, i): # This function checks the largest value from the dictionary that matches with a word, starting at a given position i.
    possible = [] #There could be multiple values that match.
    for key, values in dict.items():
        for value in values:
            if word[i:i + len(value)] == value:
                possible.append((key, value))
    if len(possible)> 0:
        longest_match = max(possible, key=lambda x: len(x[1])) # select the largest value
    else:
        longest_match = None
    if longest_match != None and len(longest_match[1])>0:
        return longest_match # return the (key,value) pair if there is one.

def conversor(*words):
    word = ''
    for i in words:
        i = str(i).replace(" ", "")
        word += i
    new_word = ""
    i = 0
    real_word = ""
    possible = []
    possible2 = False
    for key, values in diclave.items():
        for value in values:
            while i < len(word):
                match = checker(word, diclave, i)
                match2 = checker(word, diclave, i - 1)
                if match != None:
                    new_word += match[0]
                    i += len(match[1])
                elif match2 and len(match2[1]) > 1:
                    new_word += match2[0]
                    i += len(match2[1]) - 1
                else:
                    new_word = ''
                    i = 0
                    break
    if new_word != '' and new_word != word:
        return (f'{new_word} = {word}')


def conversorb(word):
    new_word = ""
    i = len(word)
    real_word = ""
    while i > 0:
        possible = []
        possible2 = False
        for key, values in diclave.items():
            for value in values:
                if word[(i-len(value)):i]  == value:
                    possible.append((key,value))

                elif word[0:i] == value[len(value)-i:len(value)]:
                    possible2 = True
                    i = 0
        if len(possible) > 0:
            longest_match = max(possible, key= lambda x: len(x[1]))
            new_word = longest_match[0] + new_word
            i -= len(longest_match[1])
        elif possible2 == True:
            real_word = word
        else:
            new_word = ''
            break
    if real_word != '':

        return (real_word)
    elif new_word != "":
        return word

print(conversor('seneca'))


x= (list(filter(None,(map(conversor,All_Words)))))

with open("Converted_Words_Spanish.txt.txt", "w") as file:
    for item in set(x):
        file.write(item + '\n')
