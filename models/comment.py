from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from datetime import date
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.article import Article

@pymongo
@jsonclass
class Comment(BaseObject):
    publish_date: Optional[str] = types.date
    content: str = types.str.required
    article: Article = types.instanceof('Article').linkto.required
    publisher: str = types.str.required