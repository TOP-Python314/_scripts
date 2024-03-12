from dataclasses import dataclass
from enum import Enum


@dataclass
class Contact:
    mobile: str
    office: str
    telegram: str
    web: str


# приблизительно эквивалентно следующему объявлению:
# class Contact:
#     def __init__(
#             self,
#             mobile: str,
#             office: str,
#             telegram: str,
#             web: str,
#     ):
#         self.mobile = mobile
#         self.office = office
#         self.telegram = telegram
#         self.web = web



class Degree(Enum):
    CANDIDATE = 'кандидат'
    DOCTOR = 'доктор'



