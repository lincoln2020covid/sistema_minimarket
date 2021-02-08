from helpers.menu import Menu
#from controllers.venta import VentaController
#from controllers.inventario import InventarioController
from controllers.administrador import AdministradorController
#from controllers.usuario import PeriodoController
#from controllers.salon import SalonController
#from controllers.factura import FacturaController
from controllers.cajero import CajeroController
from controllers.almacen import AlmacenController
#from controllers.dventa import DventaController
#from controllers.producto import ProductoController

def app():
    try:
        print('''
        =============================
            Sistema de Minimarket
        =============================
        ''')
        menu_principal = ["Administrador", "Cajero", "Almacen"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            administrador = AdministradorController()
            administrador.menu()
            if administrador.salir:
                app()
        elif respuesta == 2:
            cajero = CajeroController()
            cajero.menu()
            if cajero.salir:
                app()
        elif respuesta == 3:
            almacen = AlmacenController()
            almacen.menu()
            if almacen.salir:
                app()
#        elif respuesta == 4:
#            usuario = PeriodoController()
#            usuario.menu()
#            if usuario.salir:
#                app()
#        elif respuesta == 5:
#            salon = SalonController()
#            salon.menu()
#            if salon.salir:
#                app()
#        elif respuesta == 6:
#            dventa = DventaController()
#            dventa.menu()
#            if dventa.salir:
#                app()
#        elif respuesta == 7:
#            producto = ProductosController()
#            producto.menu()
#            if nota.salir:
#                app()

        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()



#        menu_principal = ["Usuarios", "Productos", "Inventarios", "Ventas", "Facturas", \
#        "Detalles de venta", "Salir"]
#        respuesta = Menu(menu_principal).show()
#        if respuesta == 1:
#            venta = VentaController()
#            venta.menu()
#            if venta.salir:
#                app()
#        elif respuesta == 2:
#            factura = CategoriaController()
#            factura.menu()
#            if factura.salir:
#                app()
#        elif respuesta == 3:
#            inventario = ClienteController()
#            inventario.menu()
#            if inventario.salir:
#                app()
#        elif respuesta == 4:
#            usuario = PeriodoController()
#            usuario.menu()
#            if usuario.salir:
#                app()
#        elif respuesta == 5:
#            salon = SalonController()
#            salon.menu()
#            if salon.salir:
#                app()
#        elif respuesta == 6:
#            dventa = DventaController()
#            dventa.menu()
#            if dventa.salir:
#                app()
#        elif respuesta == 7:
#            producto = ProductosController()
#            producto.menu()
#            if nota.salir:
#                app()