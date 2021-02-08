#from models.factura import Factura
#from helpers.menu import Menu
#from helpers.helper import input_data, print_table, question
#
#
#class FacturaController:
#    def __init__(self):
#        self.factura = Factura()
#        self.salir = False
#
#    def menu(self):
#        try:
#            while True:
#                print('''
#                ==================
#                    Facturas
#                ==================
#                ''')
#                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
#                respuesta = Menu(lista_menu).show()
#
#                if respuesta == 1:
#                    self.all_facturas()
#                elif respuesta == 2:
#                    self.search_factura()
#                elif respuesta == 3:
#                    self.insert_factura()
#                else:
#                    self.salir = True
#                    break
#        except Exception as e:
#            print(f'{str(e)}')
#
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
#
#    def insert_factura(self):
#        nombre_factura = input_data('Ingrese el nombre de factura >> ')
#        self.factura.insert_factura({
#            'nombre_categoria': nombre_categoria
#        })
#        print('''
#        ================================
#            Nueva factura agregado
#        ================================
#        ''')
#        self.all_categorias()
#
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

