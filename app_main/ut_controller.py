#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:08:18 2017

@author: ness
"""

"""
ut_controller: controller for main app
"""

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

 
def setup_app(app):
    """Register the routes and view functions for the given app"""

    @app.route('/geocoding/')
    @app.route('/geocoding/<search_address>')    
    def geocoding(search_address=None):
        return render_template('ut_geocoding.html', search_address=search_address)
 
def app_factory(name=__name__, debug=False):
    """Generate an instance of the app"""
    app = Flask(name)
    app.debug = debug
    setup_app(app)
    return app
 
if __name__ == '__main__':
    # Run the app
    app = app_factory(debug=True)
    app.run()