# -*- coding: utf-8 -*

from flask import Flask

from common.cache import cache

"""
export FLASK_APP=ml \
export FLASK_ENV=development \
export APP_CONFIG_FILE=/root/dev.py \
flask run --host=0.0.0.0 --port=5000
gunicorn --bind :5000 app:app --log-level=debug -w 3 -t 2 --error-logfile test.log -t 240 -k gevent
gunicorn -c /root/api/conf/gunicorn_conf.py app:app
"""

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')
app.config.from_pyfile("conf/flask-caching.conf")
app.config['JSON_AS_ASCII'] = False

with app.app_context():
        cache.init_app(app)

        from route import api, service

        app.register_blueprint(api.bp)
        app.register_blueprint(service.bp)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)