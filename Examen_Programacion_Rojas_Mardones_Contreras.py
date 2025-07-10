#Examen
#Pybooks

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def menu():
    while True:
        try:
            print("\n****Menú Principal****")
            print("1. Stock Marca")
            print("2. Busqueda Precio")
            print("3. Actualizar Precio")
            print("4. Salir")

            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Debe seleccionar una opción válida!!")
        except ValueError:
            print("Debe ingresar un número entero válido.")

def stock_marca(marca):
    marca_lower = marca.lower()
    total_stock = 0
    modelos_encontrados = []
    
    for modelo, datos in productos.items():
        if datos[0].lower() == marca_lower:
            if modelo in stock:
                total_stock += stock[modelo][1]
                modelos_encontrados.append(modelo)
    
    print(f"\nStock para la marca {marca.capitalize()}:")
    for modelo in modelos_encontrados:
        print(f"Modelo {modelo}: {stock[modelo][1]} unidades")
    print(f"Total stock: {total_stock} unidades")

def búsqueda_precio(p_min, p_max):
    resultados = []
    
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    
    resultados.sort()
    
    if resultados:
        print("\nNotebooks encontrados en el rango de precios:")
        for item in resultados:
            print(item)
    else:
        print("\nNo hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def main():
    while True:
        opcion = menu()
        
        if opcion == 1:
            print("\nOpción seleccionada: Stock Marca")
            marca = input("Ingrese la marca a consultar: ")
            stock_marca(marca)
            
        elif opcion == 2:
            print("\nOpción seleccionada: Búsqueda por Precio")
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    búsqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            
        elif opcion == 3:
            print("\nOpción seleccionada: Actualizar Precio")
            while True:
                modelo = input("Ingrese el modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if actualizar_precio(modelo, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("El precio debe ser un valor entero!!")
                
                continuar = input("¿Desea actualizar otro precio? (si/no): ").lower()
                if continuar != 'si':
                    break
                    
        elif opcion == 4:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()