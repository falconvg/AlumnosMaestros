import web

db_host = 'jj820qt5lpu6krut.cbetxkdyhwsb.us-east-1.rds.amazonaws.com	'
db_name = 'gkikf0shbqq8jonf'
db_user = 'e9otwnhxe2p20tbn'
db_pw = 'yf2sy2f06iq450eu'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
