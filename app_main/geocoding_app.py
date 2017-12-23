#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:04:48 2017

@author: ness
"""
import os, binascii
import requests
from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SECRET_KEY'] =  binascii.hexlify(os.urandom(24))  # Used for CSRF
api = Api(app)

app_id = '' # please add your app_id 
app_code = '' # please add your app_code 
gmap_ke = '' # please add you google map key here
class NoQuery(Resource):
    @app.route("/geocoding/")
    def geocdoing_noquery():
        return('please specify a location, for example: geocoding/vancouver')


class SearchQuery(Resource):
    # endpoint to get search_address
    @app.route("/geocoding/<string:search_address>", methods=["GET"])
    def geocdoing(search_address):
        # using app_id and app_code from 90 days trial of here
        url_here = 'https://geocoder.cit.api.here.com/6.2/geocode.json?app_id='+ app_id +'&app_code=' + app_code +'&searchtext='+ search_address
        r = requests.get(url_here)
        if (r.ok):
            rj = r.json()
            lat = rj['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
            lng = rj['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']      
            result = 'lat = ' + str(lat) + ', lng = '+ str(lng) 
            return(jsonify(result))
        else:
            #using my own googlemap generated key
            url_google = 'https://maps.googleapis.com/maps/api/geocode/json?address='+search_address+',CA&key='+ gmap_key
            r = requests.get(url_google)
            if (r.ok):
                rj = r.json()
                lat = rj['results'][0]['geometry']['location']['lat']
                lng = rj['results'][0]['geometry']['location']['lng']      
                result = 'lat = ' + str(lat) + ', lng = '+ str(lng) 
                return(jsonify(result))
        return('Please Modify Your Search Location!')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Not Found

api.add_resource(NoQuery, '/geoencoding')
api.add_resource(SearchQuery, '/geoencoding/<string:search_address>')

if __name__ == '__main__':
    app.run(debug=True, port=5000) # debug flag is on to show python errors