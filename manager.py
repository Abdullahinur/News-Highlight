from app import create_app
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)
manager.add_comand('server', Server)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestResult(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
