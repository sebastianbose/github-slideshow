"""Sports property scoring model.

This module provides a `SportsProperty` dataclass and a `SportsPropertyScorer`
class with a simple weighted scoring algorithm. Metrics should be provided on a
scale from 0.0 to 1.0. The scorer returns a value between 0 and 100.
"""

from dataclasses import dataclass
from typing import Dict

@dataclass
class SportsProperty:
    popularity: float = 0.0
    revenue: float = 0.0
    audience_size: float = 0.0
    social_media_presence: float = 0.0
    growth_potential: float = 0.0

class SportsPropertyScorer:
    weights: Dict[str, float] = {
        "popularity": 0.25,
        "revenue": 0.25,
        "audience_size": 0.2,
        "social_media_presence": 0.15,
        "growth_potential": 0.15,
    }

    @classmethod
    def score(cls, prop: SportsProperty) -> float:
        """Return a 0-100 score for the given sports property."""
        total = 0.0
        for metric, weight in cls.weights.items():
            value = getattr(prop, metric, 0.0)
            value = max(0.0, min(1.0, value))  # clamp to 0-1
            total += value * weight
        return round(total * 100, 2)

if __name__ == "__main__":
    example = SportsProperty(
        popularity=0.9,
        revenue=0.85,
        audience_size=0.8,
        social_media_presence=0.75,
        growth_potential=0.7,
    )
    print("Example property score:", SportsPropertyScorer.score(example))
