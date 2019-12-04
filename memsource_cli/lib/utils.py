#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os
import json
import sys
import re
import datetime


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


def get_filename(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def validate_response(response, status_code):
    if response.status_code != status_code:
        print("Memsource API Error")
        print("Error: %s" % json.loads(response.text)["errorCode"])
        print("Error description: %s" %
              json.loads(response.text)["errorDescription"])
        print("Response status: %s" % response.status_code)
        sys.exit()


def _url(self, api_version, path):
    return self.app.configuration.host + '/api2/' + ''.join(api_version) + path


def _print_output(response):
    column_header = []
    values = []
    output = response.to_dict()

    for k, v in output.items():
        column_header += [(k)]
        if isinstance(v, datetime.datetime):
            v = json.dumps(v, default=str).replace('"', '')
        if isinstance(v, dict):
            v = json.dumps(v)
        values += [(v)]
    header = tuple(column_header)
    data = tuple(values)

    return((header), (data))
