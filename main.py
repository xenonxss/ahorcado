import random
import os

def main(word, word_letters):
    
    os.system('cls')
    
    #print(f'La palabra es {word} shhhh')

    vidas = 10
    letras_adivinadas = []

    while len(word_letters) != 0:

        r = input()
        os.system('cls')
        iter = 0
        done = False
        

        for x in word_letters:

            if x == r:

                letras_adivinadas.append(r)

                print(f'[+]Muy bien, adivinaste la letra "{r}"\n [+]Letras adivinadas: {letras_adivinadas}')
               

                word_letters.remove(r)
                #print(word_letters)

                iter = iter + 1

                if len(word_letters) == 0:
                    print('[+]Ganaste o_O')

                done = True

                break

        if done == True:
            pass
        else:

            vidas = vidas - 1

            print(f'[-]Fallaste... te quedan {vidas}\n [+]Letras adivinadas: {letras_adivinadas}')

            if vidas == 0:
                return print('[-]Perdiste :(\n[i]La palabra era {word}') 
    

if '__main__' == __name__:

    palabras = ['carro', 'hotel', 'farola', 'ordenador', 'puerta', 'mesa']
    palabra_secreta = palabras[random.randrange(0, len(palabras))]
    letras_palabra = list(palabra_secreta)

    main(palabra_secreta, letras_palabra)
