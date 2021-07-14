# establish some defaults that can be overridden
ARG OPENAPI_GENERATOR_VERSION=5.2.0

##############################
#          BUILDER           #
##############################
FROM ubuntu:18.04 as generator

WORKDIR /sw/

RUN apt-get update && apt-get install -y wget default-jre && rm -rf /var/lib/apt/lists/*

ARG OPENAPI_GENERATOR_VERSION
RUN mkdir src-gen && wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar -O openapi-generator-cli.jar

COPY openapi.yml /openapi/
COPY mustache/* codegen/templates/

RUN java -jar openapi-generator-cli.jar \
    generate \
    -i /openapi/openapi.yml \
    -g python-flask \
    -o ./src-gen \
    -t ./codegen/templates

##############################
#           SERVER           #
##############################
FROM python:3.5-slim as server

WORKDIR /sw/
COPY hacked_requirements.txt .
RUN pip3 install -r hacked_requirements.txt

COPY --from=generator /sw/src-gen/ /sw/src-gen/
COPY src/ src/

# These don't seem to take
ENV DISABLE_OAUTH=1
ENV DISABLE_API_KEY=1

# Softlink our backend implementation
RUN cd src-gen/openapi_server && ln -s ../../src/server_impl/


