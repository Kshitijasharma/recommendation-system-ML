# complete pipeline

"""
Recommendation pipeline.

This module orchestrates the complete StyleAI recommendation workflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

# pyrefly: ignore [missing-import]
from PIL import Image

from backend.candidate_selection import candidate_selector
from backend.embedding import embedding_generator
from backend.look_generator import look_generator
from backend.ranking import outfit_ranker
from backend.retrieval import retriever


@dataclass(frozen=True)
class RecommendationResult:
    """
    Final recommendation returned to the frontend.
    """

    query_image: Image.Image
    query_group: str
    outfits: List[Dict[str, Any]]


class RecommendationPipeline:
    """
    Orchestrates the complete recommendation workflow.
    """

    def recommend(
        self,
        image: Image.Image,
        query_group: str,
    ) -> RecommendationResult:
        """
        Generate outfit recommendations.

        Parameters
        ----------
        image : PIL.Image.Image
            Uploaded image.

        query_group : str
            Fashion group selected by the user.

        Returns
        -------
        RecommendationResult
            Ranked outfit recommendations.
        """

        # Step 1: Generate embedding
        embedding = embedding_generator.generate_embedding(image)

        # Step 2: Retrieve similar products
        retrieved_items = retriever.retrieve(embedding)

        #debug 1:
        print(retrieved_items[["fashion_group", "category"]].head(20))

        # Step 3: Candidate selection
        candidate_pools = candidate_selector.select_candidates(
            retrieved_items=retrieved_items,
            query_group=query_group,
        )

        # Step 4: Generate outfit combinations
        outfits = look_generator.generate(candidate_pools)

        # Step 5: Rank outfits
        ranked_outfits = outfit_ranker.rank(outfits, top_n=2)

        # Step 6: Return final response
        return RecommendationResult(
            query_image=image,
            query_group=query_group,
            outfits=ranked_outfits,
        )


# Shared application-wide pipeline
pipeline = RecommendationPipeline()