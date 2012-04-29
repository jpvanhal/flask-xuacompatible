import unittest

from flask import Flask
from flask.ext.xuacompatible import XUACompatible


class XUACompatibleTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        XUACompatible(app)

        @app.route('/')
        def index():
            return 'index'

        self.client = app.test_client()

    def test_sets_xuacompatible_http_header(self):
        response = self.client.get('/')
        self.assertEqual(response.headers['X-UA-Compatible'],
            'IE=edge,chrome=1')


def suite():
    return unittest.makeSuite(XUACompatibleTestCase)


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
