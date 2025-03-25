import os
import gdown

from .MedSAM_Inference import medsam_inference

__all__ = ["medsam_inference"]

CHECKPOINT_PATH = "work_dir/MedSAM/medsam_vit_b.pth"
GDRIVE_FILE_ID = "1ETWmi4AiniJeWOt6HAsYgTjYv_fkgzoN"

def download_checkpoint():
    """Download checkpoint if not found."""
    os.makedirs(os.path.dirname(CHECKPOINT_PATH), exist_ok=True)

    if not os.path.exists(CHECKPOINT_PATH):
        print(f"Downloading MedSAM checkpoint from Google Drive...")
        gdown.download(f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}", CHECKPOINT_PATH, quiet=False)
        print("Download complete.")

download_checkpoint()
