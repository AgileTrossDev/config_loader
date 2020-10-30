from dataclasses import dataclass

@dataclass
class Config:
    """Config for Foo Class"""
    p1: str
    p2: float
    p3: int = 0
