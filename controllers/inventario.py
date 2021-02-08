from models.inventario import Inventario
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class ClienteController:
    def __init__(self):
        self.inventario = Inventario()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ================
                    Inventarios
                ================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_clientes()
                elif respuesta == 2:
                    self.search_cliente()
                elif respuesta == 3:
                    self.insert_cliente()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_clientes(self):
        try:
            print('''
            ======================
                Lista Inventarios
            ======================
            ''')
            inventarios = self.inventario.get_clientes('id_cliente')
            print(print_table(inventarios, ['ID', 'nombres']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_cliente(self):
        print('''
        ====================
            Buscar Inventario
        ====================
        ''')
        try:
            id_cliente = input_data("Ingrese el ID del inventario >> ", "int")
            inventario = self.inventario.get_cliente({
                'id_cliente': id_cliente
            })
            print(print_table(inventario, ['ID', 'nombres']))

            if inventario:
                if question('¿Deseas dar mantenimiento al inventario?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_cliente(id_cliente)
                    elif respuesta == 2:
                        self.delete_cliente(id_cliente)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_cliente(self):
        nombre = input_data('Ingrese el nombre del inventario >> ')
        self.inventario.insert_cliente({
            'nombres': nombres
        })
        print('''
        ============================
            Nuevo inventario agregado
        ============================
        ''')
        self.all_clientes()

    def update_clientes(self, id_clientes):
        nombres = input_data('Ingrese el nuevo nombre del inventario >> ')
        self.inventario.update_cliente({
            'id_cliente': id_cliente
        }, {
            'nombres': nombres
        })
        print('''
        ==========================
            Inventario Actualizado
        ==========================
        ''')

    def delete_cliente(self, id_cliente):
        self.inventario.delete_cliente({
            'id_cliente': id_cliente
        })
        print('''
        ========================
            Inventario Eliminado
        ========================
        ''')
