# -*- coding: utf-8 -*-

import unittest

from nose.tools import assert_raises

from geokrety_api_exceptions import GKUnprocessableEntity
from geokrety_api_exceptions.json_api import GKJsonApiException


class TestException(unittest.TestCase):
    """Test exception basics"""

    def test_gk_json_api(self):
        exc = GKJsonApiException("Something bad on backend",
                                 source={'pointer': '/data'},
                                 title="Unknown error custom", status="599")
        self.assertEqual(exc.title, "Unknown error custom")
        self.assertEqual(exc.detail, "Something bad on backend")
        self.assertEqual(exc.status, "599")
        self.assertEqual(exc.source, {'pointer': '/data'})
        self.assertEqual(exc.to_dict(), {
            'status': '599',
            'source': {'pointer': '/data'},
            'detail': 'Something bad on backend',
            'title': 'Unknown error custom'
        })

    def test_gk_unprocessable_entity(self):
        exc = GKUnprocessableEntity("Some wrong value",
                                    {'pointer': '/attrbute/xyz'})
        self.assertEqual(exc.title, "Unprocessable Entity")
        self.assertEqual(exc.detail, "Some wrong value")
        self.assertEqual(exc.status, "422")
        self.assertEqual(exc.source, {'pointer': '/attrbute/xyz'})
        self.assertEqual(exc.to_dict(), {
            'status': '422',
            'source': {'pointer': '/attrbute/xyz'},
            'detail': 'Some wrong value',
            'title': 'Unprocessable Entity'
        })
