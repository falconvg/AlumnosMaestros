import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_maestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_maestro) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_maestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_maestro) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_maestro, **k):

    @staticmethod
    def POST_DELETE(id_maestro, **k):
    '''

    def GET(self, id_maestro, **k):
        message = None # Error message
        id_maestro = config.check_secure_val(str(id_maestro)) # HMAC id_maestro validate
        result = config.model.get_maestros(int(id_maestro)) # search  id_maestro
        result.id_maestro = config.make_secure_val(str(result.id_maestro)) # apply HMAC for id_maestro
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_maestro, **k):
        form = config.web.input() # get form data
        form['id_maestro'] = config.check_secure_val(str(form['id_maestro'])) # HMAC id_maestro validate
        result = config.model.delete_maestros(form['id_maestro']) # get maestros data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_maestro = config.check_secure_val(str(id_maestro))  # HMAC user validate
            id_maestro = config.check_secure_val(str(id_maestro))  # HMAC user validate
            result = config.model.get_maestros(int(id_maestro)) # get id_maestro data
            result.id_maestro = config.make_secure_val(str(result.id_maestro)) # apply HMAC to id_maestro
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/maestros') # render maestros delete.html 
