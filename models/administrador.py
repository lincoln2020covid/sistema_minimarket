from connection.conn import Connection


class Administrador:
    def __init__(self):
        self.model = Connection('facturas')

    def get_administradores(self, order):
        return self.model.get_all(order)

    def get_administrador(self, id_object):
        return self.model.get_by_id(id_object)

    def search_administrador(self, data):
        return self.model.get_columns(data)

    def insert_administrador(self, administrador):
        return self.model.insert(administrador)

    def update_administrador(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_administrador(self, id_object):
        return self.model.delete(id_object)
