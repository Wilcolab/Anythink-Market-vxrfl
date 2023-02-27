from pathlib import Path
import sys

from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from app.models.domain.rwmodel import RWModel


class Profile(RWModel):
    username: str
    bio: str = ""
    image: Optional[str] = None
    following: bool = False
