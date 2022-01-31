import rank.util.recall_service_client as recall_client
from random import sample

def anime_rank(context, n=20):
    recall_res = recall_client.get_recall(context.user_id)
    return sample(recall_res, n)
