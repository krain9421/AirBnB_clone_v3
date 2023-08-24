#!/usr/bin/python3
import sys

def func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

str = "car=3 ball=4 fruit=5 animal=6"
func(str)
