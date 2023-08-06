# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pytest import raises


def test_non_ascii_bytes_fail_without_encoding(harness):
    raises(UnicodeDecodeError, harness.simple, ("""
        [------------------]
        text = u'א'
        [------------------]
        %(text)s
    """, 'utf8'))

def test_non_ascii_bytes_work_with_encoding(harness):
    expected = 'א'.encode('utf8')
    actual = harness.simple(("""
        # encoding=utf8
        [------------------]
        text = u'א'
        [------------------]
        %(text)s
    """, 'utf8')).body.strip()
    assert actual == expected

def test_the_exec_machinery_handles_two_encoding_lines_properly(harness):
    expected = 'א'.encode('utf8')
    actual = harness.simple(("""\
        # encoding=utf8
        # encoding=ascii
        [------------------]
        text = u'א'
        [------------------]
        %(text)s
    """, 'utf8')).body.strip()
    assert actual == expected
