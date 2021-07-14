#!/bin/bash
docker build --target=generator -t generator-builder .
docker run --rm -it generator-builder bash