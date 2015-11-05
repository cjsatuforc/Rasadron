#!/usr/bin/env python
# Web Server - Serving Gyro, Temperature etc. data
import web  # web.py
import json

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Credentials','true')
        return json.dumps({'status':false})

if __name__ == "__main__":
    app.run()
