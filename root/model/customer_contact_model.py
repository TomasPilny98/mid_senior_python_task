from dataclasses import dataclass


@dataclass
class CustomerContactModel:
    phone_number: int
    email_address: str
