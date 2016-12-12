# -*- coding: utf-8 -*-
from .mbase import MMBase
from math import pow, exp


class MMinf(MMBase):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def pk(self):
        ro = self.ro
        for i in range(self._to):
            yield pow(ro, i) / self.factorial(i) * exp(-ro)

    @property
    def check_stable(self):
        return self._miu > 0

    def k_mean(self):
        return self.ro

    def w_ro(self):
        return 1 / self._miu
