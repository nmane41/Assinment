from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'nitin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nitin123'
app.config['MYSQL_DATABASE_DB'] = 'nitin'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)