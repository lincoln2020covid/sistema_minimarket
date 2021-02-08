from connection.conn import Connection


class Inventario:
    def __init__(self):
        self.model = Connection('inventario')

    def get_inventarios(self, order):
        return self.model.get_all(order)

    def get_inventario(self, id_object):
        return self.model.get_by_id(id_object)

    def search_inventario(self, data):
        return self.model.get_columns(data)

    def insert_inventario(self, inventario):
        return self.model.insert(inventario)

    def update_inventario(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_inventario(self, id_object):
        return self.model.delete(id_object)
