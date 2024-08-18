import random  

def juego_de_dados():  
    print("¡Bienvenido al Juego de Dados!")  
    
    while True:  
        dado1 = random.randint(1, 6)  
        dado2 = random.randint(1, 6)  
        suma = dado1 + dado2  
        print(f"Has lanzado: {dado1} y {dado2}. Suma: {suma}")  

        jugar_otra_vez = input("¿Quieres lanzar de nuevo? (s/n): ").lower()  
        if jugar_otra_vez != 's':  
            print("Gracias por jugar. ¡Hasta luego!")  
            break  

# Ejecuta el juego  
juego_de_dados()