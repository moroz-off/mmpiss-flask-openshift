# -*- coding: utf-8 -*-
from __future__ import division
from .mbase import MMBase
from math import pow


class MMVKN(MMBase):
    def __init__(self, v, a, miu, to, n):
        super().__init__(None, miu, to)
        self._a = a
        self._lambd_div_miu = a / (1 - a)
        self._v = v
        self._n = n
        self._val_pk = None

    def _pk(self):
        for k in range(self._to + 1):
            div1 = self.ccc(self._n, k) * pow(self._lambd_div_miu, k)
            div2 = sum((self.ccc(self._n, i) * pow(self._lambd_div_miu, i)) for i in range(self._v + 1))
            yield div1 / div2

    @property
    def pk(self):
        if self._val_pk:
            return self._val_pk
        self._val_pk = tuple(self._pk())
        return self._val_pk

    def check_stable(self):
        return self._miu > 0 and self._a / ((1 - self._a) * self._v) and self._n >= self._to and self._v < self._n

    def k_mean(self):
        return sum(((i * p) for i, p in zip(range(self._v + 1), self.pk)))

    def t_mean(self):
        return self.k_mean() / self._miu

    def _pt_pv(self, fn):
        div1 = self.ccc(fn, self._v) * pow(self._lambd_div_miu, self._v)
        div2 = sum(((self.ccc(fn, i) * pow(self._lambd_div_miu, i)) for i in range(self._v + 1)))

        return div1 / div2

    def pt(self):
        return self._pt_pv(self._n)

    def pv(self):
        return self._pt_pv(self._n - 1)

    def ccc(self, n, k):
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))
