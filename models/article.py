from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from datetime import date
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.user import User
    from models.comment import Comment

@pymongo
@jsonclass
class Article(BaseObject):
    name: str = types.str.required
    publish_date: Optional[str] = types.date
    content: str = types.str.required
    user: User = types.instanceof('User').linkto.required
    comments: list[Comment] = types.nonnull.listof('Comment').linkedby("article")