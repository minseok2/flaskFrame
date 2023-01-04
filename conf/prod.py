from conf.default import *
from logging.config import dictConfig

# DB type ( 1:'mysql or mariaDB', 2:'postgres', 3:'oracle' )
DB_TYPE=2
DB_PATH=os.path.join(BASE_DIR, 'conf/db.conf')

INTENT_URL="http://10.20.76.121:8501/v1/models/intentclf:predict"