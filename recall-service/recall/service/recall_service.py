from recall.context import Context
from typing import List
import recall.strategy as strategy
import concurrent.futures
import time
from recall import util


strategies: List[strategy.RecallStrategy] = [
    strategy.HighRatingStrategy(),
    strategy.MostRatingStrategy(),
]

def anime_recall(context: Context, n=20) -> List[int]:
    """
    returns a list of anime ids
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        outputs = executor.map(lambda s: run_strategy(s, context, n), strategies)
        outputs = [aid for l in outputs for aid in l]
        outputs = list(dict.fromkeys(outputs))
        print(f'Got {len(outputs)} uniq recall results')
        return outputs

def similar_animes(context: Context, n=20) -> List[int]:
    stra = strategy.SimilarAnimeStrategy()
    return stra.recall(context, n)

def run_strategy(strategy: strategy.RecallStrategy, context: Context, n):
    start_time = time.time()
    res = strategy.recall(context, n=n)
    elapse_time = time.time() - start_time
    print('Strategy %s took %.2fms' % (strategy.name(), elapse_time * 1000))
    return res
