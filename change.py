def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:")
    print(expense)
    print(f"Dinero recibido")
    print(money)
    print("\n")
    print(f"Vuelto")
    print("\n")
    change=(money-expense)    
    print(f"Pesos:")
    print(int(change))
    centavos=(change-int(change))*(int(money))
    print(f"Centavos:")
    print(int(centavos))
