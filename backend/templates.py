# pyrefly: ignore [missing-import]

# define the outfit templates

"""
Outfit template definitions.

This module contains the outfit composition rules used by the
candidate selection and look generation stages.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class OutfitTemplate:
    """
    Defines which fashion groups are needed to complete an outfit.
    """

    input_group: str
    required_groups: List[str]

OUTFIT_TEMPLATES = {
    "Topwear": OutfitTemplate(
        input_group="Topwear",
        required_groups=[
            "Bottomwear",
            "Footwear",
            "Outerwear",
            "Bag",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Bottomwear": OutfitTemplate(
        input_group="Bottomwear",
        required_groups=[
            "Topwear",
            "Footwear",
            "Outerwear",
            "Bag",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Dress": OutfitTemplate(
        input_group="Dress",
        required_groups=[
            "Footwear",
            "Outerwear",
            "Bag",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Footwear": OutfitTemplate(
        input_group="Footwear",
        required_groups=[
            "Topwear",
            "Bottomwear",
            "Outerwear",
            "Bag",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Outerwear": OutfitTemplate(
        input_group="Outerwear",
        required_groups=[
            "Topwear",
            "Bottomwear",
            "Footwear",
            "Bag",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Bag": OutfitTemplate(
        input_group="Bag",
        required_groups=[
            "Topwear",
            "Bottomwear",
            "Footwear",
            "Outerwear",
            "Jewelry",
            "Accessories",
        ],
    ),

    "Jewelry": OutfitTemplate(
        input_group="Jewelry",
        required_groups=[
            "Topwear",
            "Bottomwear",
            "Footwear",
            "Outerwear",
            "Bag",
            "Accessories",
        ],
    ),

    "Accessories": OutfitTemplate(
        input_group="Accessories",
        required_groups=[
            "Topwear",
            "Bottomwear",
            "Footwear",
            "Outerwear",
            "Bag",
            "Jewelry",
        ],
    ),
}