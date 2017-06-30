#!/usr/bin/env python3

import es_sql
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# 192.168.1.8 9300
# es_sql.execute_sql('http://192.168.1.8:9200', 'SELECT number FROM github LIMIT 10')
ESHOST = '192.168.1.8'
ESPORT = 9300
ESURL = 'http://%s:%s' % (ESHOST, ESPORT)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
	app.config.update(debug=False)
	app.run(host='0.0.0.0', port=8080)
