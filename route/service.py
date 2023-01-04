# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, request
from flask_restx import Resource, Api, reqparse, fields
from ast import literal_eval

from common.utils import *
from flask import current_app

import json as j
import os
import pickle
import requests
import core.intent as itt

bp = Blueprint('service', __name__, url_prefix='/ml')

api = Api(
    app=bp,
    version="0.1",
    title="ML engine API",
    description="ML engine API service",
    default="ML engine API",
    default_label="ml engine"
)

current_app.tokenizer = get_tokenizer()

@api.route('/cls')
class APITAKeyword(Resource):
    @staticmethod
    def post():
        items = get_items()
        text = request.json.get('text')
        return j.dumps(itt.serving(text, current_app.tokenizer, items),ensure_ascii=False)
