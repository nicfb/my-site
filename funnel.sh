#!/bin/sh
sudo tailscale funnel 8081 &
/home/nic/my-site/.venv/bin/python server.py