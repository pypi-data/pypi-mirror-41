from decimal import Decimal
from .price import Price
from .tax_class import TaxClass
from .discount import Discount
from .jsonable import Jsonable

class Item(Jsonable):
    # TODO: Change name to Orderline
    # TODO: Add images?
    def __init__(self,
                 name,                    # type: str
                 quantity,                # type: Decimal
                 unit,                    # type: str
                 unitPrice,               # type: Price
                 subtotal,                # type: Price
                 totalDiscount,           # type: Price
                 totalPrice,              # type: Price
                 taxClass,                # type: TaxClass
                 shortDescription=None,   # type: str
                 description=None,        # type: str
                 brand=None,              # type: str
                 discounts=None,          # type: List[Discount]
                 ):
        assert isinstance(name, str), "parameter should be str type"
        assert isinstance(quantity, (Decimal, int)), "parameter should be Decimal type"
        assert isinstance(unit, str), "parameter should be str type"
        assert isinstance(unitPrice, Price), "parameter should be Price type"
        assert isinstance(subtotal, Price), "parameter should be Price type"
        assert isinstance(totalDiscount, Price), "parameter should be Price type"
        assert isinstance(totalPrice, Price), "parameter should be Price type"
        assert isinstance(taxClass, TaxClass), "parameter should be TaxClass type"
        if shortDescription is not None:
            assert isinstance(shortDescription, str), "parameter should be str type"
        if description is not None:
            assert isinstance(description, str), "parameter should be str type"
        if brand is not None:
            assert isinstance(brand, str), "parameter should be str type"
        if discounts is not None:
            assert isinstance(discounts, list), "parameter should be list type"
            assert all(isinstance(x, Discount) for x in discounts), (
                "parameter should be a list of Discount objects.")
        assert subtotal.withTax - totalDiscount.withTax == totalPrice.withTax, (
            "subtotal - discount != total")
        assert subtotal.withoutTax - totalDiscount.withoutTax == totalPrice.withoutTax, (
            "subtotal - discount != total")
        assert unitPrice.withoutTax * quantity == subtotal.withoutTax, (
            "unitPrice * quantity != subtotal")
        assert unitPrice.withTax * quantity == subtotal.withTax, (
            "unitPrice * quantity != subtotal")
        assert unitPrice.tax == unitPrice.withoutTax * taxClass.fraction, (
            "Tax price not equal to tax rate")

        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unitPrice = unitPrice
        self.subtotal = subtotal
        self.totalDiscount = totalDiscount
        self.totalPrice = totalPrice
        self.taxClass = taxClass
        self.shortDescription = shortDescription
        self.description = description
        self.brand = brand
        self.discounts = discounts

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Item

        return cls(
            name=json_dict['name'],
            quantity=json_dict['quantity'],
            unit=json_dict['unit'],
            unitPrice=Price.from_json_dict(json_dict['unitPrice']),
            subtotal=Price.from_json_dict(json_dict['subtotal']),
            totalDiscount=Price.from_json_dict(json_dict['totalDiscount']),
            totalPrice=Price.from_json_dict(json_dict['totalPrice']),
            taxClass=TaxClass.from_json_dict(json_dict['taxClass']),
            shortDescription=json_dict.get('shortDescription', None),
            description=json_dict.get('description', None),
            brand=json_dict.get('brand', None),
            discounts=list(map(Discount.from_json_dict, json_dict.get('discounts', [])))
        )