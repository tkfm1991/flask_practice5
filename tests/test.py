from importlib import import_module
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        flask_app = import_module('main')
        flask_app.app.testing = True
        self.app = flask_app.app.test_client()

    def test_over18_true(self):
        name = 'sato'
        over18 = 'on'
        sex = '男'
        belong = '東京支店'
        other = 'hogehoge'
        data = dict(name=name, over18=over18, sex=sex, belong=belong, other=other)
        actual = self.app.post('/output', data=data)
        assert actual.status_code == 200
        assert name in actual.get_data(as_text=True)
        assert '18歳以上' in actual.get_data(as_text=True)

    def test_over18_false(self):
        name = 'sato'
        over18 = ''
        sex = '男'
        belong = '東京支店'
        other = 'hogehoge'
        data = dict(name=name, over18=over18, sex=sex, belong=belong, other=other)
        actual = self.app.post('/output', data=data)
        assert actual.status_code == 200
        assert name in actual.get_data(as_text=True)
        assert '18歳未満' in actual.get_data(as_text=True)
