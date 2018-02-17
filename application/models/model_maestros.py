import web
import config

db = config.db


def get_all_maestros():
    try:
        return db.select('maestros')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_maestros(id_maestro):
    try:
        return db.select('maestros', where='id_maestro=$id_maestro', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_maestros(id_maestro):
    try:
        return db.delete('maestros', where='id_maestro=$id_maestro', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_maestros(nombre,materia):
    try:
        return db.insert('maestros',nombre=nombre,
materia=materia)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_maestros(id_maestro,nombre,materia):
    try:
        return db.update('maestros',id_maestro=id_maestro,
nombre=nombre,
materia=materia,
                  where='id_maestro=$id_maestro',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
