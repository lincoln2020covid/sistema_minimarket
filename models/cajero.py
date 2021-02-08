from connection.conn import Connection


class Cajero:
    def __init__(self):
        self.model = Connection('facturas')

    def get_cajeros(self, order):
        return self.model.get_all(order)

    def get_cajero(self, id_object):
        return self.model.get_by_id(id_object)

    def search_cajero(self, data):
        return self.model.get_columns(data)

    def insert_cajero(self, cajero):
        return self.model.insert(cajero)

    def update_cajero(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_cajero(self, id_object):
        return self.model.delete(id_object)