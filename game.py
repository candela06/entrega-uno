import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Lista para almacenar las letras adivinadas
guessed_letters = []

#numero de fallos
max_fault = 5
fault = 0
levels = {
    "facil": lambda word: "".join([letter if letter in "aeiou" else "_" for letter in word]),
    "medio": lambda word: word[0] + "_" * (len(word) - 2) + word[-1],
    "dificil": lambda word: "_" * len(word)
    }

print("¡Bienvenido al juego de adivinanzas!")

while True:
    level = input("Por favor, elige un nivel de dificultad (fácil, medio, difícil): ").lower()
    if level in levels:
        print(f"Nivel: {level}")
        break
    else:
        print("Nivel de dificultad no válido. Por favor, elige entre fácil, medio o difícil.")


print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = levels[level](secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


while fault < max_fault:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada o es vacío
     if letter == '':
        print('No has ingresado ninguna letra')   
        continue
     else:
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
    
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         fault+=1
     
     # Mostrar la palabra parcialmente adivinada
     '''
     "facil": lambda word: "".join([letter if letter in "aeiou" else "_" for letter in word]),
    "medio": lambda word: word[0] + "_" * (len(word) - 2) + word[-1],
    "dificil": lambda word: "_" * len(word)
    }
     '''
     if level == 'facil':
         word_displayed = "".join([letter if letter in (guessed_letters and 'aeiou') else "_" for letter in secret_word])
         print(f"Palabra: {word_displayed}")

     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has alcanzado la cantidad máxima de fallos")
     print(f"La palabra secreta era: {secret_word}")