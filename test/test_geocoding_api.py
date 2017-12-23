"""
Created on Fri Dec 22 10:15:47 2017

@author: ness
"""
import sys
# To include the application's path in the Python search path
sys.path.append("/home/ness/Narges/AI Learning Project/X/app_main")
#print(sys.path)

#notes formyself to kill process:
##### to see the processes
# sudo lsof -i :5000
##### to kill the process
# sudo kill -9 <process_id>

import unittest
from flask_testing import TestCase  # Flask-Testing extension
from ut_controller import app_factory
from flask import url_for, request
sys.path.append("/X/app_main")
from geocoding_app import NoQuery, SearchQuery

class TestGeocodingApi(TestCase):   # from Flask-Testing Extension
    """Test Case"""
    def create_app(self):
        """
        To return a Flask app instance.
        Run before setUp() for each test method.
        Automatically setup self.app, self.client, and manage the contexts.
        """
        print('run create_app()')
        # Generate a Flask app instance and a test client for every test method
        app = app_factory(debug =True)
        app.config['TESTING'] = True        
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False # to get rid of a build error due to flask bug
        return app
     
    def setUp(self):
        """Called before each test method"""
        print('run setUp()')
 
    def tearDown(self):
        """Called after each test method"""
        print('run tearDown()')

    def test_view_geocoding_noquery(self):
        """test view function of geocoding with no query"""
        _path = url_for('geocoding')  # url_for() needs app context
        self.assertEqual(request.path, '/')  
        response = self.client.get(_path)  # Send GET request and retrieve the response
        self.assertEqual(response.status_code, 200)

 
    def test_view_geocoding(self):
        """test view function geocoding"""
        _search_address = 'Vancouver'
        _path = url_for('geocoding', search_address=_search_address)
        response = self.client.get(_path)
        self.assertEqual(response.status_code, 200)
 
    def test_geocoding_noquery(self):
        response = NoQuery.geocdoing_noquery()
        self.assertEqual(response,'please specify a location, for example: geocoding/vancouver')

    def test_geocoding(self):
        response = SearchQuery.geocdoing('Vancouver')
        self.assertIn("lat = 49.26039, lng = -123.11336",(response.data.decode("utf-8"))) # response from here

        

if __name__ == "__main__":
    unittest.main()