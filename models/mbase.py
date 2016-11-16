# -*- coding: utf-8 -*-
from json import dumps
from math import factorial


class MMBase(object):
    def __init__(self, lambd, miu, to):
        self._lambd = lambd
        self._miu = miu
        self._to = to

    @property
    def ro(self):
        return self._lambd / self._miu

    @property
    def pk(self):
        yield ()

    def check_stable(self):
        raise NotImplementedError()

    @staticmethod
    def factorial(x):
        return factorial(x)

    def get_json(self):
        return dumps(tuple(self.pk))

    def __bool__(self):
        return self.check_stable()
