
from django.test import SimpleTestCase

import requests
from django.test.runner import DiscoverRunner
import os, django, sys, inspect
os.environ['DJANGO_SETTINGS_MODULE'] = 'hyper_resource_py.settings'
django.setup()
from bcim.models import *

#python manage.py test hyper_resource.tests_cache --testrunner=hyper_resource.tests_cache.NoDbTestRunner
class NoDbTestRunner(DiscoverRunner):
   """ A test runner to test without database creation/deletion """

   def setup_databases(self, **kwargs):
     pass

   def teardown_databases(self, old_config, **kwargs):
     pass


#python manage.py test bcim.test_utils  --testrunner=bcim.test_utils.NoDbTestRunner
from django.test import SimpleTestCase

class APIAbstractResourceCacheTestCase(SimpleTestCase):
    def setUp(self):
        #self.host = 'luc00557347.ibge.gov.br'
        self.host = 'luc00557196.ibge.gov.br:8000'
        self.url_feature_resource_collection = 'http://' + self.host + '/ibge/bcim/aldeias-indigenas/'
        self.url_feature_resource = 'http://' + self.host + '/ibge/bcim/aldeias-indigenas/'
        self.headers = {'accept': 'application/octet-stream', 'If-None-Match': '48200128876656848'}


    def test_headers_for_lists(self):
        self.url_feature_resource_collection = 'http://' + self.host + '/ibge/bcim/aldeias-indigenas/'
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertEquals(res.headers['content-type'], 'application/octet-stream')
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': 'application/octet-stream', 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 304)

        self.headers = {'accept': 'application/vnd.geo+json'}
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.headers['content-type'] == 'application/vnd.geo+json')
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': 'application/vnd.geo+json', 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 304)
        self.headers = {'accept': 'application/octet-stream'}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': 'application/octet-stream', 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 304)

    def test_headers_feature_resource_operations(self):
        self.url_feature_resource = 'http://' + self.host + '/ibge/bcim/unidades-federativas/ES/buffer/1.2'
        self.headers = {'accept': 'application/vnd.geo+json'}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.headers['content-type'] == 'application/vnd.geo+json')
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': 'application/vnd.geo+json', 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 304)

        self.headers = {'accept': 'application/octet-stream'}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertEquals(res.headers['content-type'], 'application/octet-stream')
        self.assertTrue(res.status_code == 200)

    def test_headers_feature_resource_operation_area(self):
        self.url_feature_resource = 'http://' + self.host + '/ibge/bcim/unidades-federativas/ES/area'
        ct = 'application/json'
        self.headers = {'accept': ct}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.headers['content-type'] == ct)
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': ct, 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.status_code == 304)
        self.url_feature_resource = 'http://' + self.host + '/ibge/bcim/unidades-federativas/ES/transform/3005&True/area'
        res = requests.get(self.url_feature_resource)
        self.assertEquals(res.headers['content-type'], ct)
        self.assertTrue(res.status_code == 200)
        self.headers = {'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource, headers=self.headers)
        self.assertTrue(res.headers['content-type'] == ct)
        self.assertTrue(res.status_code == 200)


    def test_headers_for_lists_attributes(self):
        self.url_feature_resource_collection = 'http://' + self.host + '/ibge/bcim/unidades-federativas/nome,sigla'
        self.headers = {'accept': 'application/json'}
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.headers['content-type'] == 'application/json')
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 200)
        self.headers = {'accept': 'application/json', 'If-None-Match': res.headers['etag']}
        res = requests.get(self.url_feature_resource_collection, headers=self.headers)
        self.assertTrue(res.status_code == 304)


