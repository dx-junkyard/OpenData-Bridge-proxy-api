from dataclasses import dataclass

@dataclass
class Link:
    href: str
    text: str

@dataclass
class ExtractLinks:
    links: list[Link]