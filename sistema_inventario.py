class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or not isinstance(nombre, str) or not str(nombre).strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero.")
            
        self.nombre = str(nombre).strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        
    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El nuevo precio debe ser un número mayor o igual a cero.")
        self.precio = float(nuevo_precio)
        
    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La nueva cantidad debe ser un número entero mayor o igual a cero.")
        self.cantidad = int(nueva_cantidad)
        
    def calcular_valor_total(self):
        return self.precio * self.cantidad
        
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto al inventario.")
        self.productos.append(producto)
        
    def buscar_producto(self, nombre):
        if not nombre:
            return None
        nombre_lower = str(nombre).strip().lower()
        for p in self.productos:
            if p.nombre.lower() == nombre_lower:
                return p
        return None
        
    def calcular_valor_inventario(self):
        return sum(p.calcular_valor_total() for p in self.productos)
        
    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\n--- Lista de Productos en Inventario ---")
        for p in self.productos:
            print(p)
        print("----------------------------------------")


def menu_principal():
    inventario = Inventario()
    
    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            try:
                nombre = input("Ingrese el nombre del producto: ")
                precio_str = input("Ingrese el precio del producto: ")
                cantidad_str = input("Ingrese la cantidad del producto: ")
                
                # Validar y convertir tipos
                precio = float(precio_str)
                # Considerar cantidades con decimales como inválidas para la entrada de este campo
                if '.' in cantidad_str:
                    raise ValueError("La cantidad debe ser un número entero.")
                cantidad = int(cantidad_str)
                
                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"¡Producto '{nombre}' agregado exitosamente!")
                
            except ValueError as e:
                print(f"\nError de entrada: {e}")
            except Exception as e:
                print(f"\nError inesperado: {e}")
                
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto_encontrado = inventario.buscar_producto(nombre)
            
            if producto_encontrado:
                print("\nProducto encontrado:")
                print(producto_encontrado)
            else:
                print(f"\nNo se encontró ningún producto con el nombre '{nombre}'.")
                
        elif opcion == '3':
            inventario.listar_productos()
            
        elif opcion == '4':
            valor_total = inventario.calcular_valor_inventario()
            print(f"\nEl valor total del inventario es: ${valor_total:.2f}")
            
        elif opcion == '5':
            print("Saliendo del sistema de inventario. ¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo con un número del 1 al 5.")


if __name__ == "__main__":
    menu_principal()
