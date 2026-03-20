import random

words = {
    "programacion": ["python", "variable", "funcion"],
    "animales": ["perro", "gato", "leon",],
    "frutas": ["manzana", "pera", "naranja"]
}

print("¡Bienvenido al Ahorcado!")
print()

#Mostras las categorias disponibles
print("Tipos de categorias:")
for category in words:
    print(f"            {category}")

#Verificar que haya ingresado correctamente la categoria
found = False
while not found:
    selection = input("Ingrese la categoria: ").lower()
    found = selection in words 
    if not found:
        print("Por favor ingrese una categoria correctamente.")
        print()

shuffled_words = random.sample(words[selection], len(words[selection]))

total_points = 0

for word in shuffled_words:
    guessed = []
    attempts = 6
    points = 6
    
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            points += 6
            print(f"¡Ganaste!. Tu puntos fueron : {points} puntos.")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()

        #Verificar que sea solo UNA letra
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            print()
            continue
    
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            points -= 1
            print("Esa letra no está en la palabra.")
        
        print()
    else:
        points = 0
        print(f"¡Perdiste! La palabra era: {word}. Tu puntos fueron : {points} puntos.")

    total_points += points

print("Fin.")
print(f"Puntuacion total alcanzada: {total_points} puntos")