from models.inventario import Inventario
from models.almacen import Almacen
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class AlmacenController:
    def __init__(self):
        self.inventario = Inventario()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Inventario
                ==================
                ''')
                lista_menu = ["Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.insert_inventario()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

#    def all_facturas(self):
#        try:
#            print('''
#            ==========================
#                Listar Facturas
#            ==========================
#            ''')
#            facturas = self.factura.get_facturas('id_factura')
#            print(print_table(facturas, ['ID', 'fecha', 'producto', 'cantidad_vendida', 'precio_unitario', 'monto_factura']))
#            input('\nPresiona una tecla para continuar...')
#        except Exception as e:
#            print(f'{str(e)}')
#
#    def search_factura(self):
#        print('''
#        ========================
#            Buscar Factura
#        ========================
#        ''')
#        try:
#            id_factura = input_data("Ingrese el ID del factura >> ", "int")
#            factura = self.factura.get_factura({
#                'id_factura': id_factura
#            })
#            print(print_table(factura, ['ID', 'fecha', 'producto', 'cantidad_vendida', 'precio_unitario', 'monto_factura']))
#
#            if factura:
#                if question('¿Deseas dar mantenimiento al factura?'):
#                    opciones = ['Editar', 'Eliminar', 'Salir']
#                    respuesta = Menu(opciones).show()
#                    if respuesta == 1:
#                        self.update_factura(id_factura)
#                    elif respuesta == 2:
#                        self.delete_factura(id_factura)
#        except Exception as e:
#            print(f'{str(e)}')
#        input('\nPresiona una tecla para continuar...')

    def insert_inventario(self):
        fecha = input_data('Ingrese la fecha de ingreso de producto al inventario >> ')
        categoria = input_data('Ingrese la categoria >> ')
        precio_unitario = input_data('Ingrese el precio unitario >> ')
        compras = input_data('Ingrese las compras >> ')
        ventas = input_data('Ingrese las ventas >> ')
        stock = input_data('Ingrese las stock >> ')
        producto = input_data('Ingrese el producto >> ')
        self.inventario.insert_inventario({
            'fecha': fecha,
            'categoria': categoria,
            'precio_unitario': precio_unitario,
            'compras': compras,
            'ventas': ventas,
            'stock': stock,
            'producto': producto,
        })
        print('''
        ============================================
            Nuevo ingreso a inventario completado
        ============================================
        ''')
#        self.all_facturas()

#    def update_categoria(self, id_categoria):
#        nombre_categoria = input_data('Ingrese el nuevo nombre de factura >> ')
#        self.factura.update_categoria({
#            'id_categoria': id_categoria
#        }, {
#            'nombre_categoria': nombre_categoriao
#        })
#        print('''
#        ============================
#            Factura Actualizada
#        ============================
#        ''')
#
#    def delete_categoria(self, id_categoria):
#        self.factura.delete_categoria({
#            'id_categoria': id_categoria
#        })
#        print('''
#        =========================
#            Factura Eliminada
#        =========================
#        ''')

