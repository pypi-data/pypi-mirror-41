from decimal import Decimal
from .jsonable import Jsonable

class Price(Jsonable):
    def __init__(self,
                 withoutTax, # type: Decimal
                 withTax,    # type: Decimal
                 tax         # type: Decimal
                 ):
        assert isinstance(withoutTax, (Decimal, int)), "parameter should be Decimal type"
        assert isinstance(withTax, (Decimal, int)), "parameter should be Decimal type"
        assert isinstance(tax, (Decimal, int)), "parameter should be Decimal type"
        assert withoutTax + tax == withTax, "tax does not add up."
        self.withoutTax = withoutTax
        self.withTax = withTax
        self.tax = tax

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Price

        return cls(**json_dict) 