meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "TANKAR": "suportar ou resistir a algo, geralmente dor",
            "QUEBRAR": "ser pego desprevinido de alguma maneira",
            "FARMAR": "acumular recursos"
            }

print("Muito prazer, aqui é um dicionário de modernismos")
print("Pergunte o significado de cinco delas por favor")

for i in range(5):
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas):")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print(word, "não foi encontrado nesta enciclopédia de palavras usuais")
