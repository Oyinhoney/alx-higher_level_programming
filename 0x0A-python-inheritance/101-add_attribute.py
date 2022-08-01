#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon 1st August 2022
@author: Adeyemi Adedoyin
"""


def add_attribute(obj, name, value):
    """
    Add attribute into the class if it's possible
    Arguments:
        obj (object): The object to set as attribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
