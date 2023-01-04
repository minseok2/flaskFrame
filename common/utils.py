import configparser

from common.cache import cache
from common.database import Database
from common.encryption import EnDecrypt

from flask import current_app
from transformers import BertTokenizer

# DB 정보 암호화
def set_crypto(config_parser, path):
    id = config_parser.get('db-info', 'id')
    pw = config_parser.get('db-info', 'pw')
    enDecrypt = EnDecrypt()
    key = enDecrypt.get_key()
    crypto_id = enDecrypt.encrypt(id)
    crypto_pw = enDecrypt.encrypt(pw)

    config_parser.set('db-info', 'key', key.decode())
    config_parser.set('db-info', 'crypto_id', crypto_id)
    config_parser.set('db-info', 'crypto_pw', crypto_pw)
    config_parser.remove_option('db-info', 'id')
    config_parser.remove_option('db-info', 'pw')

    with open(path, 'w') as configfile:
        config_parser.write(configfile)

def get_db_info(path):
    config_parser = configparser.RawConfigParser()
    config_parser.read(path)

    if 'id' in config_parser['db-info'] and 'pw' in config_parser['db-info']:
        set_crypto(config_parser, path)

    simpleEnDecrypt = EnDecrypt(config_parser.get('db-info', 'key'))
    cryto_id = config_parser.get('db-info', 'crypto_id')
    id = simpleEnDecrypt.decrypt(cryto_id)

    cryto_pw = config_parser.get('db-info', 'cryto_pw')
    pw = simpleEnDecrypt.decrypt(cryto_id)

    host = config_parser.get('db-info', 'host')
    port = config_parser.get('db-info', 'port')
    db_name = config_parser.get('db-info', 'db')

    return host, port, id, pw, db

@cache.cached(key_prefix='get_items')
def get_items():
    sql = "select number, intent_nm from intent where order by seq"

    db = Database()
    items = {i[0]:i[1] for i in db.executeAll(sql)}
    db.close()
    return items

def get_tokenizer(name='monologg/koelectra-base-v3-discriminator'):
    return BertTokenizer.from_pretrained(name)

    