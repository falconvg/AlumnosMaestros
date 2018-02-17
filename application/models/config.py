import web

db_host = 'localhost'
db_name = 'unid_alumnos'
db_user = 'unid'
db_pw = 'unidalumnos5'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )