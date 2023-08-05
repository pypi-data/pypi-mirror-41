#!/bin/bash
uwsgi \
  --http-socket 0.0.0.0:8180 \
  --master \
  --die-on-term \
  --module pacifica.proxy.wsgi "$@"
