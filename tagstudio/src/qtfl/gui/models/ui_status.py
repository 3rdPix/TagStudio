from dataclasses import dataclass
from typing import Any

@dataclass
class NavigationState:
    contents: Any
    scrollbar_pos: int
    page_index: int
    page_count: int
    search_text: str | None = None,
    thumb_size = None,
    spacing = None