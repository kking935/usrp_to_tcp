#!/usr/bin/env bash
./top_block.py &
sleep 3
./zmq_sub.py
