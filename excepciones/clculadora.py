class Calculadora:
    def __init__(self):
        while True:
            try:
                self.numero1 = float(input('Ingresa un número (decimal): '))
                self.numero2 = float(input('Ingresa otro número (decimal): '))
                break
            except ValueError as e:
                print(f'Error: {e}. Por favor, ingresa un número decimal válido.')

    def suma(self):
        return self.numero1 + self.numero2

    def resta(self):
        return self.numero1 - self.numero2

    def multi(self):
        return self.numero1 * self.numero2

    def division(self):
        try:
            return self.numero1 / self.numero2
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == '1':
                print(f"Resultado: {self.suma()}")
            elif opcion == '2':
                print(f"Resultado: {self.resta()}")
            elif opcion == '3':
                print(f"Resultado: {self.multi()}")
            elif opcion == '4':
                print(f"Resultado: {self.division()}")
            elif opcion == '5':
                print("¡Adiós!")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

# Ejecución
calc = Calculadora()
calc.menu()
