import cv2
import numpy as np
import matplotlib.pyplot as plt

# ── CONFIG ────────────────────────────────────────────────
IMAGE_PATH   = "powder.jpg"
TARGET_SIZES = [1024, 512, 256, 128, 64, 32]
# ─────────────────────────────────────────────────────────

# Load image and convert BGR (OpenCV default) to RGB (for matplotlib)
img = cv2.imread(IMAGE_PATH)
original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = original.shape[:2]

print(f"Image loaded: {w}x{h} px")

# ── Overview: all sizes in one figure ────────────────────
fig, axes = plt.subplots(1, len(TARGET_SIZES) + 1, figsize=(28, 5))

axes[0].imshow(original)
axes[0].set_title(f"Original\n{w}x{h}")
axes[0].axis("off")

for i, size in enumerate(TARGET_SIZES, start=1):
    # Shrink to target size, then blow back up so pixelation is visible
    small    = cv2.resize(original, (size, size), interpolation=cv2.INTER_NEAREST)
    restored = cv2.resize(small,    (w, h),        interpolation=cv2.INTER_NEAREST)

    axes[i].imshow(restored)
    axes[i].set_title(f"{size}x{size}")
    axes[i].axis("off")

plt.suptitle("Spatial Sampling -- Resolution Reduction", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("sampling_overview.png", dpi=150, bbox_inches="tight")
plt.show()

# ── Individual figures: original | small | upscaled ──────
for size in TARGET_SIZES:
    small    = cv2.resize(original, (size, size), interpolation=cv2.INTER_NEAREST)
    restored = cv2.resize(small,    (w, h),        interpolation=cv2.INTER_NEAREST)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Sampling to {size}x{size} px", fontweight="bold")

    axes[0].imshow(original);  axes[0].set_title(f"Original ({w}x{h})");          axes[0].axis("off")
    axes[1].imshow(small);     axes[1].set_title(f"Downsampled ({size}x{size})");  axes[1].axis("off")
    axes[2].imshow(restored);  axes[2].set_title("Upscaled back (pixelated)");     axes[2].axis("off")

    plt.tight_layout()
    plt.savefig(f"sampling_{size}px.png", dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved: sampling_{size}px.png")
