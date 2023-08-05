from datetime import datetime
from decimal import Decimal
import dateutil.parser
import simplejson 

from .price import Price
from .item import Item
from .payment import Payment
from .vendor import Vendor
from .fee import Fee
from .loyalty import Loyalty
from .jsonable import Jsonable

def default_ser(obj):
    if hasattr(obj, 'jsonable'):
        return obj.jsonable()
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return simplejson.dumps(obj, 
            sort_keys=True)

class Receipt(Jsonable):
    # TODO: add totalChange?
    # TODO: Add cashier?
    # TODO: Make totalDiscount and totalFee optional?
    # NOTE: 'global' discounts should be applied to individual items
    def __init__(self, 
                 time,                    # type: datetime 
                 currency,                # type: str
                 subtotal,                # type: Price
                 totalDiscount,           # type: Price
                 totalPrice,              # type: Price
                 totalFee,                # type: Price
                 totalPaid,               # type: Decimal
                 items,                   # type: List[Item]
                 payments,                # type: List[Payment]
                 vendor,                  # type: Vendor
                 vendorReference,         # type: str
                 fees=None,               # type: List[Fee]
                 loyalties=None,          # type: List[Loyalty]
                 ):
        # type: () -> None
        assert isinstance(time, datetime), "parameter should be datetime type"
        assert isinstance(currency, str), "parameter should be str type"
        assert isinstance(subtotal, Price), "parameter should be Price type"
        assert isinstance(totalDiscount, Price), "parameter should be Price type"
        assert isinstance(totalPrice, Price), "parameter should be Price type"
        assert isinstance(totalFee, Price), "parameter should be Price type"
        assert isinstance(totalPaid, (Decimal, int)), "parameter should be Decimal type"
        assert isinstance(items, list), "parameter should be list type"
        assert all(isinstance(x, Item) for x in items), (
            "parameter should be a list of Item objects.")
        assert isinstance(payments, list), "parameter should be list type"
        assert all(isinstance(x, Payment) for x in payments), (
            "parameter should be a list of Payment objects.")
        assert isinstance(vendor, Vendor), "parameter should be Vendor type"
        assert isinstance(vendorReference, str), "parameter should be str type"
        if fees is not None:
            assert isinstance(fees, list), "parameter should be list type"
            assert all(isinstance(x, Fee) for x in fees), (
                "parameter should be a list of Fee objects.")
        if loyalties is not None:
            assert isinstance(loyalties, list), "parameter should be list type"
            assert all(isinstance(x, Loyalty) for x in loyalties), (
                "parameter should be a list of Loyalty objects.")
        assert sum(map(lambda i: i.subtotal.withoutTax, items)) == subtotal.withoutTax, (
            "items subtotal does not add up to subtotal")
        assert sum(map(lambda p: p.amount, payments)) == totalPaid, (
            "payments do not add up to totalPaid")
        # TODO: assert discounts add up
        # TODO: assert fees add up
        # TODO: assert totalPrice adds up
        self.time = time
        self.currency = currency
        self.subtotal = subtotal
        self.totalDiscount = totalDiscount
        self.totalPrice = totalPrice
        self.totalFee = totalFee
        self.totalPaid = totalPaid
        self.items = items
        self.payments = payments
        self.vendor = vendor
        self.vendorReference = vendorReference
        self.fees = fees
        self.loyalties = loyalties

    def to_json(self):
        # type: () -> str
        return simplejson.dumps(self, sort_keys=True, default=default_ser)

    @classmethod
    def from_json(cls, json_str):
        # type: (str) -> Receipt
        json_dict = simplejson.loads(json_str, use_decimal=True)
        return cls.from_json_dict(json_dict)
    
    @classmethod
    def from_json_dict(cls, json_dict):
        return cls(
            time=dateutil.parser.parse(json_dict['time']),
            currency=json_dict['currency'],
            subtotal=Price.from_json_dict(json_dict['subtotal']),
            totalDiscount=Price.from_json_dict(json_dict['totalDiscount']),
            totalPrice=Price.from_json_dict(json_dict['totalPrice']),
            totalFee=Price.from_json_dict(json_dict['totalFee']),
            totalPaid=json_dict['totalPaid'],
            items=list(map(Item.from_json_dict, json_dict['items'])),
            payments=list(map(Payment.from_json_dict, json_dict['payments'])),
            vendor=Vendor.from_json_dict(json_dict['vendor']),
            vendorReference=json_dict['vendorReference'],
            fees=list(map(Fee.from_json_dict, json_dict.get('fees', []))),
            loyalties=list(map(Loyalty.from_json_dict, json_dict.get('loyalties', [])))
        )