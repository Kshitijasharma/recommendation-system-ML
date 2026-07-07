"""
Download all images from the Marqo Polyvore dataset.

Images are saved locally using their item_ID as the filename.

Example:
    data/polyvore_images/12345678.jpg
"""

from pathlib import Path

# pyrefly: ignore [missing-import]
from datasets import load_dataset
# pyrefly: ignore [missing-import]
from PIL import Image
from tqdm import tqdm
import pandas as pd


DATASET_NAME = "Marqo/polyvore"
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "data" / "polyvore_images"
METADATA_PATH = PROJECT_ROOT / "models" / "retrieval" / "metadata.csv"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load metadata to filter out unnecessary images if metadata.csv exists
    valid_ids = None
    if METADATA_PATH.exists():
        print(f"Loading metadata from {METADATA_PATH} to filter items...")
        df = pd.read_csv(METADATA_PATH)
        valid_ids = set(df["item_ID"].astype(str))
        print(f"Found {len(valid_ids):,} valid item IDs in metadata.")
    else:
        print("Metadata file not found, downloading all dataset images...")

    print("Loading dataset from Hugging Face...")
    dataset = load_dataset(DATASET_NAME, split="data")

    print(f"Dataset size: {len(dataset):,} images")

    saved_count = 0
    for sample in tqdm(dataset):
        item_id = str(sample["item_ID"])
        if valid_ids is not None and item_id not in valid_ids:
            continue

        image: Image.Image = sample["image"]
        
        # Ensure we convert RGBA images to RGB before saving as JPEG
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        image.save(
            OUTPUT_DIR / f"{item_id}.jpg",
            quality=95,
        )
        saved_count += 1

    print(f"Download completed. Saved {saved_count:,} images to {OUTPUT_DIR}.")


if __name__ == "__main__":
    main()