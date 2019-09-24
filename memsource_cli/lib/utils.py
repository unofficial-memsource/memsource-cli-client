#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os
import json
import sys

API_URL = 'https://cloud.memsource.com/web/api2/'


def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars
    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.
    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


def validate_response(response, status_code):
    if response.status_code != status_code:
        print("Memsource API Error")
        print("Error: %s" % json.loads(response.text)["errorCode"])
        print("Error description: %s" %
              json.loads(response.text)["errorDescription"])
        print("Response status: %s" % response.status_code)
        sys.exit()


def _url(api_version, path):
    return API_URL + ''.join(api_version) + path


def _print_output(response):
    column_header = []
    values = []
    output = response.to_dict()

    for k, v in output.items():
        column_header += [(k)]
        values += [(v)]
    header = tuple(column_header)
    data = tuple(values)

    return((header), (data))
