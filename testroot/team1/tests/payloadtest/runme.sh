#!/bin/bash
# a test that shows how payloads come along

grep -q 'themagicstring' ./payload  || exit 1
grep -q 'yetanotherstring' ./somedir/another_payload || exit 1
grep -q 'thirdone' ./d1/d2/d3/thirdfile || exit 1
exit 0
