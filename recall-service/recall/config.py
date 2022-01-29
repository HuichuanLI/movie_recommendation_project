import os

config = {
    'dataset_path': os.environ['DATASET_PATH'],
    'most_rating': {
        'shuffle_sample': True
    },
    'high_rating': {
        'shuffle_sample': True
    }
}
