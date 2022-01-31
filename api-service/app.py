# -*- coding:utf-8 -*-
# @Time : 2022/1/31 11:14 下午
# @Author : huichuan LI
# @File : app.py
# @Software: PyCharm
from flask import Flask, jsonify, request
import api.rank_service_client as rank_client
from api.anime import get_anime

app = Flask('api-service')


@app.route("/")
def get_recommends():
    user_id = request.args.get('user_id', type=int)
    rec_anime_ids = rank_client.get_anime(user_id)
    res = [get_anime(id) for id in rec_anime_ids]

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/sim")
def get_similar_animes():
    anime_id = request.args.get('anime_id', type=int)
    if anime_id is None:
        return 'bad anime id', 400

    sim_anime_ids = rank_client.get_similar_anime(anime_id)
    res = [get_anime(id) for id in sim_anime_ids]

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/anime/<id>")
def get_anime_by_id(id):
    res = get_anime(id)
    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
