#!/bin/bash
export $(cat .env | xargs) && python3 api.py
