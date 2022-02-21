# -*- coding:utf-8 -*-
# @Time : 2022/1/31 11:14 下午
# @Author : huichuan LI
# @File : app.py
# @Software: PyCharm

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
from flask import Flask, jsonify, request
import api.rank_service_client as rank_client
from api.anime import get_anime

app = Flask('api-service')


@app.route("/")
def get_recommends():
    user_id = request.args.get('user_id', type=int)
    rec_animes = rank_client.get_anime(user_id)
    for item in rec_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = rec_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/sim")
def get_similar_animes():
    anime_id = request.args.get('anime_id', type=int)
    if anime_id is None:
        return 'bad anime id', 400

    sim_animes = rank_client.get_similar_anime(anime_id)
    for item in sim_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = sim_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/anime/<id>")
def get_anime_by_id(id):
    res = get_anime(id)
    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
