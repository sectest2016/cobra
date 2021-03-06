#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    cobra
    ~~~~~

    Implements cobra main

    :author:    BlBana <635373043@qq.com>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
from cobra.parser import scan_parser
from cobra.config import project_directory


target_projects = project_directory + '/tests/vulnerabilities/v_parser.php'
with open(target_projects, 'r') as fi:
    code_contents = fi.read()

sensitive_func = ['system']
lineno = 7


def test_scan_parser():
    assert scan_parser(code_contents, sensitive_func, lineno)
