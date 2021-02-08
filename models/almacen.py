from connection.conn import Connection


class Almacen:
    def __init__(self):
        self.model = Connection('inventario')

    def get_almacenes(self, order):
        return self.model.get_all(order)

    def get_almacen(self, id_object):
        return self.model.get_by_id(id_object)

    def search_almacen(self, data):
        return self.model.get_columns(data)

    def insert_almacen(self, almacen):
        return self.model.insert(almacen)

    def update_almacen(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_almacen(self, id_object):
        return self.model.delete(id_object)