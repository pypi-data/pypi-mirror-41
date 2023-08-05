from .price import Price
from .tax_class import TaxClass
from .jsonable import Jsonable

class Fee(Jsonable):
    def __init__(self,
                 name,    # type: str
                 price,   # type: Price
                 taxClass # type: TaxClass
                 ):
        assert isinstance(name, str), "parameter should be str type"
        assert isinstance(price, Price), "parameter should be Price type"
        assert isinstance(taxClass, TaxClass), "parameter should be TaxClass type"
        assert price.tax == price.withoutTax * taxClass.fraction, (
            "Tax price not equal to tax rate")
        self.name = name
        self.price = price
        self.taxClass = taxClass

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Fee

        return cls(
            name=json_dict['name'],
            price=Price.from_json_dict(json_dict['price']),
            taxClass=TaxClass.from_json_dict(json_dict['taxClass'])
        )