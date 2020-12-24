#!/bin/bash -xe

DATE="$(date +%Y%m%d)"
WORKSPACE=${WORKSPACE:-$PWD}
echo "$WORKSPACE"

DOCKER_BUILD_IMAGE=math-mouse-base
docker build --no-cache \
    -f Dockerfile.base \
    -t $DOCKER_BUILD_IMAGE:${DATE} .

docker tag $DOCKER_BUILD_IMAGE:${DATE} $DOCKER_BUILD_IMAGE:latest
