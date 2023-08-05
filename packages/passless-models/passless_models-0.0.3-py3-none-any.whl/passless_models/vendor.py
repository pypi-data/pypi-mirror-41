from .jsonable import Jsonable

class Vendor(Jsonable):
    # TODO: Include difference between company and shop
    # TODO: Validate logo, find a decent logo format
    # TODO: Change kvkNumber to 'company registry'
    def __init__(self,
                 name,      # type: str
                 address,   # type: str
                 phone,     # type: str
                 vatNumber, # type: str
                 kvkNumber, # type: str
                 logo=None, # type: str
                 email=None,# type: str
                 web=None,  # type: str
                 meta=None, # type: dict
                 ):
        assert isinstance(name, str), "parameter should be str type"
        assert isinstance(address, str), "parameter should be str type"
        assert isinstance(phone, str), "parameter should be str type"
        assert isinstance(vatNumber, str), "parameter should be str type"
        assert isinstance(kvkNumber, str), "parameter should be str type"
        if logo is not None:
            assert isinstance(logo, str), "parameter should be str type"
        if email is not None:
            assert isinstance(email, str), "parameter should be str type"
        if web is not None:
            assert isinstance(web, str), "parameter should be str type"
        if meta is not None:
            assert isinstance(meta, dict), "parameter should be dict type"
        self.name = name
        self.address = address
        self.phone = phone
        self.vatNumber = vatNumber
        self.kvkNumber = kvkNumber
        self.logo = logo
        self.email = email
        self.web = web
        self.meta = meta

    @classmethod
    def from_json_dict(cls, json_dict):
        # type: (dict) -> Vendor

        return cls(**json_dict)