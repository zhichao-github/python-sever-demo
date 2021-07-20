from enum import Enum
from jsonclasses import jsonenum


@jsonenum
class Sex(Enum):
    MALE = 1
    FEMALE = 2