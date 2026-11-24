import cv2
import numpy as np
import matplotlib.pyplot as plt

# ── CONFIG ─────────────────────────────────────────────────
IMAGE_PATH = "powder.jpg"
BIT_DEPTHS = [8, 7, 6, 5, 4, 3, 2, 1]
# ───────────────────────────────────────────────────────────

# Load image and convert BGR (OpenCV) to RGB (matplotlib)
original = cv2.cvtColor(cv2.imread(IMAGE_PATH), cv2.COLOR_BGR2RGB)

# Quantization: reduce each pixel value to only 2^bits discrete levels
# Formula: floor(v / step) * step  where step = 256 / 2^bits
def quantize(image, bits):
    step = 256 / (2 ** bits)
    return np.clip(np.floor(image.astype(np.float32) / step) * step, 0, 255).astype(np.uint8)

# ── Summary table ───────────────────────────────────────────
print(f"{'Bits':>5}  {'Levels/ch':>10}  {'Total colors':>15}  {'Data/pixel':>12}")
print("-" * 50)
for bits in BIT_DEPTHS:
    lvl = 2 ** bits
    tag = " << original" if bits == 8 else ""
    print(f"{bits:>5}  {lvl:>10,}  {lvl**3:>15,}  {bits*3:>9} bits{tag}")

# ── Overview: all bit depths in one figure ──────────────────
fig, axes = plt.subplots(1, len(BIT_DEPTHS) + 1, figsize=(36, 5))
axes[0].imshow(original);  axes[0].set_title("Original\n8-bit");  axes[0].axis("off")

for i, bits in enumerate(BIT_DEPTHS, start=1):
    lvl = 2 ** bits
    axes[i].imshow(quantize(original, bits))
    axes[i].set_title(f"{bits}-bit\n{lvl} levels/ch")
    axes[i].axis("off")

plt.suptitle("Color Quantization -- Bit-Depth Reduction", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("quantization_overview.png", dpi=150, bbox_inches="tight")
plt.show()

# ── Individual figures: original | quantized | histogram ────
for bits in BIT_DEPTHS:
    lvl     = 2 ** bits
    q_image = quantize(original, bits)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle(f"Quantization -- {bits}-bit ({lvl} levels/ch)", fontweight="bold")

    axes[0].imshow(original);  axes[0].set_title("Original (8-bit)");             axes[0].axis("off")
    axes[1].imshow(q_image);   axes[1].set_title(f"{bits}-bit ({lvl**3:,} colors)"); axes[1].axis("off")

    # Histogram: smooth curve = many levels, tall spikes = few levels (banding)
    axes[2].hist(original[:, :, 0].ravel(), bins=256, range=(0,256), color="salmon",  alpha=0.5, label="Original")
    axes[2].hist(q_image[:, :, 0].ravel(),  bins=256, range=(0,256), color="darkred", alpha=0.7, label=f"{bits}-bit")
    axes[2].set_xlabel("Pixel intensity (0-255)")
    axes[2].set_ylabel("Pixel count")
    axes[2].legend(fontsize=8)
    axes[2].set_title("Red Channel Histogram")

    plt.tight_layout()
    plt.savefig(f"quantization_{bits}bit.png", dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Saved: quantization_{bits}bit.png")
