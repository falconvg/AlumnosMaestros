import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_maestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_maestro) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_maestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_maestro) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_maestro, **k):

    @staticmethod
    def POST_EDIT(id_maestro, **k):
        
    '''

    def GET(self, id_maestro, **k):
        message = None # Error message
        id_maestro = config.check_secure_val(str(id_maestro)) # HMAC id_maestro validate
        result = config.model.get_maestros(int(id_maestro)) # search for the id_maestro
        result.id_maestro = config.make_secure_val(str(result.id_maestro)) # apply HMAC for id_maestro
        return config.render.edit(result, message) # render maestros edit.html

    def POST(self, id_maestro, **k):
        form = config.web.input()  # get form data
        form['id_maestro'] = config.check_secure_val(str(form['id_maestro'])) # HMAC id_maestro validate
        # edit user with new data
        result = config.model.edit_maestros(
            form['id_maestro'],form['nombre'],form['materia'],
        )
        if result == None: # Error on udpate data
            id_maestro = config.check_secure_val(str(id_maestro)) # validate HMAC id_maestro
            result = config.model.get_maestros(int(id_maestro)) # search for id_maestro data
            result.id_maestro = config.make_secure_val(str(result.id_maestro)) # apply HMAC to id_maestro
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/maestros') # render maestros index.html
