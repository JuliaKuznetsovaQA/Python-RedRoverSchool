from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None,
    last_name: str = None,
    full_name: str = None,
    address: str = None,
    phone_number: str = None