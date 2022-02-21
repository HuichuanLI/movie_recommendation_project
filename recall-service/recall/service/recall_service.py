from recall.context import Context
from typing import List
import recall.strategy as strategy
import concurrent.futures
import time
from recall import util
from recall.dataset.embedding import get_one_item_embedding

strategies: List[strategy.RecallStrategy] = [
    strategy.HighRatingStrategy(),
    strategy.MostRatingStrategy(),
    strategy.UserEmbeddingStrategy(),
]


def anime_recall(context: Context, n=20) -> List[int]:
    """
    returns a list of anime ids
    """
    experiment_strategies = strategies
    bucket = util.bucketize(context.user_id, 2)
    if bucket == 1:
        experiment_strategies = strategies[1:]
    print(f"user_id {context.user_id}, experiment {bucket}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        outputs = executor.map(lambda s: run_strategy(s, context, n), experiment_strategies)
        outputs = [aid for l in outputs for aid in l]
        outputs = list(dict.fromkeys(outputs))
        print(f'Got {len(outputs)} uniq recall results')
        return [{'anime_id': id, 'ab:recall': bucket} for id in outputs]


def similar_animes(context: Context, n=20) -> List[int]:
    lsh = get_item_lsh()
    target_item_emb = get_one_item_embedding(context.anime_id)
    outputs = lsh.search(target_item_emb, n=n)
    return [{'anime_id': id} for id in outputs]


def run_strategy(strategy: strategy.RecallStrategy, context: Context, n):
    start_time = time.time()
    res = strategy.recall(context, n=n)
    elapse_time = time.time() - start_time
    print('Strategy %s took %.2fms' % (strategy.name(), elapse_time * 1000))
    return res
