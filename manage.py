from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flaskRest.app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__== '__main__':
	manager.run()




# from flask.cli 
# import FlaskGroup
# from flaskRest.app import app
# cli = FlaskGroup(app)


# @cli.command(‘test’)
# @click.argument(‘test_case’, default=’test*.py’)
# def test(test_case=’test*.py’):



# if __name__ == "__main__":
# cli()