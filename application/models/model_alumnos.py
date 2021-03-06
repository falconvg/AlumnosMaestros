import web
import config

db = config.db


def get_all_alumnos():
    try:
        return db.select('alumnos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_alumnos(id_alumno):
    try:
        return db.select('alumnos', where='id_alumno=$id_alumno', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_alumnos(id_alumno):
    try:
        return db.delete('alumnos', where='id_alumno=$id_alumno', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_alumnos(nombre,domicilio,telefono,maestria):
    try:
        return db.insert('alumnos',nombre=nombre,
domicilio=domicilio,
telefono=telefono,
maestria=maestria)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_alumnos(id_alumno,nombre,domicilio,telefono,maestria):
    try:
        return db.update('alumnos',id_alumno=id_alumno,
nombre=nombre,
domicilio=domicilio,
telefono=telefono,
maestria=maestria,
                  where='id_alumno=$id_alumno',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
