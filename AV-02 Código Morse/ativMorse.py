# PROGRAMAÇÃO ORIENTADA AO OBJETO - P7 de Informática
# Prof: Taveira
# Aluno: Kelvin de Lima Rodrigues

dicionarioMorse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": ".._.",
        "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....","6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": " "}
# dicionário criado para armazenar os caracteres em código morse


linhaUm = '+'+('-'*60)+'+' # string criada para dividir as mensagens na tela e deixar a vizualização mais amigável
print(linhaUm)
print("| TRADUTOR DE CÓDIGO MORSE :-)"+(' '*31)+'|')
print(linhaUm)

print("SPOILER: tudo o que vc escrever vai sair em código morse ><")
fraseOriginal = input("Digite algo para transliterar:\n") # usuário entra com o texto a ser traduzido
fraseCodificada = ''

for caractere in fraseOriginal:
    if caractere != '' and caractere.lower() in dicionarioMorse: # verifica se o caractere pertence ao dicionário 'dicionarioMorse'
        fraseCodificada += dicionarioMorse[caractere.lower()] # se pertencer, adiciona o caractere à string 'fraseCodificada'

print(linhaUm)
print("Texto original: ", fraseOriginal) 
print("Texto codificado: ", fraseCodificada) # texto codificado é mostrado ao usuário
print(linhaUm)
print("| Fim da execução :-)"+(' '*40)+'|')
print(linhaUm)
