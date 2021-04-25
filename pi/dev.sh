#!/bin/bash
PGUSER=kegweight \
PGHOST=127.0.0.1 \
PGPASSWORD=kegpass \
PGDATABASE=kegweight \
PGPORT=5432 \
KEG_ID=left_tap \
DEBUG=true \
DISABLE_SERIAL=true \
  python3 ./read-and-store.py


  