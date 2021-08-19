#!/bin/bash
# Only status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
