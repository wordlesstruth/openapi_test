#!/bin/bash
docker build -t openapi .
docker run -it --name=openapi --rm -p 8080:8080 -w '/sw/src-gen/'  openapi:latest "python3" "-m" "openapi_server"