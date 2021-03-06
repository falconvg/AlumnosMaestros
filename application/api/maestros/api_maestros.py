import web
import config
import json


class Api_maestros:
    def get(self, id_maestro):
        try:
            # http://0.0.0.0:8080/api_maestros?user_hash=12345&action=get
            if id_maestro is None:
                result = config.model.get_all_maestros()
                maestros_json = []
                for row in result:
                    tmp = dict(row)
                    maestros_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(maestros_json)
            else:
                # http://0.0.0.0:8080/api_maestros?user_hash=12345&action=get&id_maestro=1
                result = config.model.get_maestros(int(id_maestro))
                maestros_json = []
                maestros_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(maestros_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            maestros_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestros_json)

# http://0.0.0.0:8080/api_maestros?user_hash=12345&action=put&id_maestro=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,materia):
        try:
            config.model.insert_maestros(nombre,materia)
            maestros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestros_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_maestros?user_hash=12345&action=delete&id_maestro=1
    def delete(self, id_maestro):
        try:
            config.model.delete_maestros(id_maestro)
            maestros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestros_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_maestros?user_hash=12345&action=update&id_maestro=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_maestro, nombre,materia):
        try:
            config.model.edit_maestros(id_maestro,nombre,materia)
            maestros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestros_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            maestros_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestros_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_maestro=None,
            nombre=None,
            materia=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_maestro=user_data.id_maestro
            nombre=user_data.nombre
            materia=user_data.materia
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_maestro)
                elif action == 'put':
                    return self.put(nombre,materia)
                elif action == 'delete':
                    return self.delete(id_maestro)
                elif action == 'update':
                    return self.update(id_maestro, nombre,materia)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
