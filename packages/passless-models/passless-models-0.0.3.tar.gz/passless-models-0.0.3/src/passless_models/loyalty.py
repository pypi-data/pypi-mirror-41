from decimal import Decimal
from datetime import datetime
import dateutil.parser
from .jsonable import Jsonable

class Loyalty(Jsonable):
    def __init__(self,
                 points,         # type: Decimal
                 validUntil=None # type: datetime
                 ):
        assert isinstance(points, (Decimal, int)), "parameter should be Decimal type"
        if validUntil is not None:
            assert isinstance(validUntil, datetime), "parameter should be datetime type"
        self.points = points
        self.validUntil = validUntil

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Loyalty

        return cls(
            points=json_dict['points'],
            validUntil=dateutil.parser.parse(json_dict['validUntil'])
        )