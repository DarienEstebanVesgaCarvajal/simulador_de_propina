import os

def desing():
    invalidInputMessage = "Error: Ingresa un número válido 1, 2 o 3."
    while True:
        try:
            print(f"""
            =============================================
                         SELECCIÓN DE USER
            =============================================
            1. Clientela.
            2. Administración.
            3. Salir
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-3): "))
            
            if selectedOption in [1, 2, 3]:
                os.system('clear')
                return selectedOption
            else:
                print(invalidInputMessage)
        
        except ValueError:
            print(invalidInputMessage)
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para salir.")