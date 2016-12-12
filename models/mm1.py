# -*- coding: utf-8 -*-
from .mbase import MMBase
from math import pow


class MM1(MMBase):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def pk(self):
        ro = self.ro
        for i in range(self._to):
            yield (1 - ro) * pow(ro, i)

    @property
    def check_stable(self):
        return self._lambd / self._miu < 1

    def k_mean(self):
        ro = self.ro
        return ro / (1 - ro)

    def lq(self):
        ro = self.ro
        return ro * ro / (1 - ro)

    def ws(self):
        return 1 / (self._miu - self._lambd)

    def wq(self):
        ro = self.ro
        return ro / (self._miu * (1 - ro))
