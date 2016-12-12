# -*- coding: utf-8 -*-
from __future__ import division
from .mbase import MMBase
from math import pow


class MMVK(MMBase):
    def __init__(self, v, lambd, miu, to):
        super().__init__(lambd, miu, to)
        self._v = v

    @property
    def pk(self):
        ro = self.ro
        div2 = sum((pow(ro, i) / self.factorial(i)) for i in range(self._v + 1))

        for i in range(self._to + 1):
            yield (pow(ro, i) / self.factorial(i)) / div2

    @property
    def check_stable(self):
        return self.ro / self._v <= 1

    def pt(self):
        ro = self.ro
        div1 = pow(ro, self._v) / self.factorial(self._v)
        div2 = sum(((pow(ro, i) / self.factorial(i)) for i in range(self._v + 1)))

        return div1 / div2
