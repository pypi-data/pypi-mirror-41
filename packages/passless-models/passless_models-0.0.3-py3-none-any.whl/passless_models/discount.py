from .price import Price
from .jsonable import Jsonable

class Discount(Jsonable):
    # TODO: Add description
    def __init__(self,
                 name,     # type: str
                 deduct    # type: Price
                 ):
        assert isinstance(name, str), "parameter should be str type"
        assert isinstance(deduct, Price), "parameter should be Price type"
        self.name = name
        self.deduct = deduct

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Discount

        return cls(
            name=json_dict['name'],
            deduct=Price.from_json_dict(json_dict['deduct'])
        )