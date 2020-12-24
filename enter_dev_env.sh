#!/usr/bin/env sh

REPO="math-mouse"
CONTAINER="$REPO-container"
IMAGE="$REPO-base"

# Test if the container is running
HASH=$(docker ps -q -f name=$CONTAINER)

# Test if the container is stopped
HASH_STOPPED=$(docker ps -qa -f name=$CONTAINER)
if [ -n "$HASH" ]; then
  echo "founding existing running container $CONTAINER, proceeed to exec another shell"
  docker exec -it $HASH
elif [ -n "$HASH_STOPPED" ]; then
  echo "founding existing stopped container $CONTAINER, proceeed to start"
  docker start --attach -i $HASH_STOPPED
else
  echo "existing container not found, createing a new one, named $CONTAINER"
  docker run --name=${CONTAINER} -it -v $PWD:/$REPO -w /$REPO -i "$IMAGE"
fi
echo "see you, use 'docker rm $CONTAINER' to kill the vm if you want a fresh env next time"
