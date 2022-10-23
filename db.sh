#!/bin/bash

docker run \
  -d \
  -e POSTGRES_DB=expt \
  -e POSTGRES_USER=tester \
  -e POSTGRES_PASSWORD=abcd \
  -v $(realpath ./storage/pg/data):/var/lib/postgresql/data \
  -p 5434:5432 \
  postgres:12.1
