from pathlib import Path
import sys
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: Optional[str]
    body: Optional[str]
