# -*- coding: utf-8 -*-
from __future__ import division
from .mbase import MMBase
from math import pow


class MMV(MMBase):
    def __init__(self, v, lambd, miu, to):
        super().__init__(lambd, miu, to)
        self._v = v

    @property
    def pk(self):
        ro = self.ro
        znam = sum((pow(ro, i) / self.factorial(i)) for i in range(self._v))
        znam += pow(ro, self._v) * self._v / (self.factorial(self._miu) * (self._v - ro))
        sep = self._v if self._to > self._v else self._to

        for i in range(sep + 1):
            yield pow(ro, i) / self.factorial(i) / znam

        if not self._to > self._v:
            return

        for i in range(self._to - self._v + 1):
            yield pow(ro, self._v) / self.factorial(self._v) * pow(ro / self._v, i) / znam

    def check_stable(self):
        return self.ro / self._v <= 1

    def gamma_mean(self):
        return 1 / (self._miu * (self._v - self.ro))

    def j_mean(self):
        return self.gamma_mean() * self._lambd

    def pt(self):
        ro = self.ro
        a = (pow(ro, self._v) / self.factorial(self._v)) * (self._v / (self._v - ro))
        summ = sum(((pow(ro, i) / self.factorial(i)) for i in range(self._v)))

        b = summ + (pow(ro, self._v) * self._v) / (self.factorial(self._v) * (self._v - ro))
        return a / b
