#!/bin/sh

if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='../dataset/'
fi

python -m recall.bin.train