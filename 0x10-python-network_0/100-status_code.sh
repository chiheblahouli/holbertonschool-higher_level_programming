#!/bin/bash
# displays status of response code.
curl -so /dev/null -w "%{http_code}" "$1"
