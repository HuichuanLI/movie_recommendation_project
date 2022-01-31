# -*- coding:utf-8 -*-
# @Time : 2022/1/31 11:16 下午
# @Author : huichuan LI
# @File : rank_service_client.py
# @Software: PyCharm
import requests
from api.config import config


def get_anime(user_id):
    params = {}
    if user_id is not None:
      params['user_id'] = user_id
    res = requests.get(config['rank_endpoint'], params=params)
    res.raise_for_status()
    return res.json()

def get_similar_anime(anime_id):
    params = {}
    params['anime_id'] = anime_id
    res = requests.get(config['recall_endpoint'] + "/sim", params=params)
    res.raise_for_status()
    return res.json()
