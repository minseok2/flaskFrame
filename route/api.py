# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, request, redirect, url_for
from flask_restx import Resource, Api
from common.utils import *

import json as j
import os
import subprocess


bp = Blueprint('api', __name__)

api = Api(
    app=bp,
    version="0.1",
    title="ML engine API",
    description="ML engine API util Function",
    default="ML engine API",
    default_label="ml engine"
)

@api.route('/ping')
class Ping(Resource):
    @staticmethod
    def get():
        return "success"

# 재 학습 파이프라인 실행
@api.route('/retrain')
class ModelRetrain(Resource):
    @staticmethod
    def post():
        return "success"


# 모델 리스트 출력
@api.route('/list')
class ModelList(Resource):
    @staticmethod
    def post():
        return "success"
