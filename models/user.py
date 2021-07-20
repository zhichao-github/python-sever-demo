from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from datetime import date
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
from models.sex import Sex
if TYPE_CHECKING:
    from models.article import Article

@pymongo
@jsonclass
class User(BaseObject):
    name: Optional[str] = types.str.unique.maxlength(16)
    password: str = types.str.writeonly.required
    email: Optional[str] = types.str.unique
    sex: Optional[Sex] = types.enum(Sex).writeonce 
    date_of_birth: Optional[data] = types.date
    articles: list[Article] = types.nonnull.listof('Article').linkedby('user')

