import os
import gdown

CHECKPOINT_PATH = "work_dir/MedSAM/medsam_vit_b.pth"
GDRIVE_FILE_ID = "1UAmWL88roYR7wKlnApw5Bcuzf2iQgk6_"

def download_checkpoint():
    """Download checkpoint if not found."""
    os.makedirs(os.path.dirname(CHECKPOINT_PATH), exist_ok=True)

    if not os.path.exists(CHECKPOINT_PATH):
        print(f"Downloading MedSAM checkpoint from Google Drive...")
        gdown.download(f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}", CHECKPOINT_PATH, quiet=False)
        print("Download complete.")

download_checkpoint()

from .MedSAM_Inference import medsam_inference, show_mask, show_box, preprocess, visualize_results

__all__ = ["medsam_inference", "show_mask", "show_box", "preprocess", "visualize_results"]