#!/bin/bash

BIN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
ROOT_DIR="$(dirname $BIN_DIR)";
DOCKER_COMPOSE="${ROOT_DIR}/docker-compose.yml";

docker-compose -f ${DOCKER_COMPOSE} up;
