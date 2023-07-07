"""Redefines asdict() method of @dataclass"""

from dataclasses import asdict


class Base:
    """To exclude chosen attr from result dict"""

    _exclude = None

    def _asdict(self):
        res = asdict(self)
        if self._exclude:
            for attr in self._exclude:
                res.pop(attr, None)
        return res
