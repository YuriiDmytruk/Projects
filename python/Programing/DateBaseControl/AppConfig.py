from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:alchemy123@localhost:3306/customers_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
