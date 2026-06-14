#!/bin/bash

case "$1" in
    build_generator)
        docker build -t csv-generator .
        ;;
    run_generator)
        mkdir -p ./data
        docker run --rm -v "$(pwd)/data:/data" csv-generator python generate.py /data
        ;;
    create_local_data)
        mkdir -p ./local_data
        python generate.py ./local_data
        ;;
    build_reporter)
        docker build -f Dockerfile.reporter -t csv-reporter .
        ;;
    run_reporter)
        mkdir -p ./data
        docker run --rm -v "$(pwd)/data:/data" csv-reporter node report.js /data/data.csv /data/report.html
        ;;
esac