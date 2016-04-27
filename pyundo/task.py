# encoding: utf8
from __future__ import absolute_import, print_function


class TaskBase(object):
    def do(self):
        raise NotImplemented

    def undo(self):
        raise NotImplemented
