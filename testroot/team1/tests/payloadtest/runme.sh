#!/bin/bash
# a test that shows how payloads come along

grep -q 'themagicstring' ./payload && exit 0 || exit 1
