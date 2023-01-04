import multiprocessing
import os
CURR_DIR = os.getcwd()

api_home = CURR_DIR

chdir = api_home

bind = '0.0.0.0:5000'

workers = multiprocessing.cpu_count() * 2 + 1

threads = 4

worker_class = 'gevent'

timeout = 120

reload = False

limit_request_line = 100000

daemon=True

pidfile = api_home + '/pid/gunicorn.pid'

errorlog = api_home + '/logs/gunicorn.log'

max_requests = 300

max_requests_jitter = 50
