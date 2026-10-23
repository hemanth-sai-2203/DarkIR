import time
from pathlib import Path
import torch
from PIL import Image
from torchvision.transforms.functional import to_tensor, to_pil_image
from archs.DarkIR import DarkIR

input_dir = Path("images/inputs")
output_dir = Path("images/results")
output_dir.mkdir(parents=True, exist_ok=True)
input_dir.mkdir(parents=True, exist_ok=True)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = DarkIR(
    img_channel=3, width=32,
    middle_blk_num_enc=2, middle_blk_num_dec=2,
    enc_blk_nums=[1, 2, 3], dec_blk_nums=[3, 1, 1],
    dilations=[1, 4, 9], extra_depth_wise=True
)

checkpoint = torch.load(
    "models/DarkIR_384.pt", map_location="cpu", weights_only=False
)
weights = checkpoint["params"]
if weights and all(k.startswith("module.") for k in weights):
    weights = {k.removeprefix("module."): v for k, v in weights.items()}

model.load_state_dict(weights, strict=True)
model.to(device).eval()
print("Model loaded on:", device)

files = sorted(
    p for p in input_dir.iterdir()
    if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".webp"}
)

if not files:
    print("Put at least one low-light image in images/inputs/ and rerun.")
    raise SystemExit(0)

for path in files:
    image = Image.open(path).convert("RGB")
    x = to_tensor(image).unsqueeze(0).to(device)

    start = time.time()
    with torch.inference_mode():
        y = model(x).clamp(0, 1)

    destination = output_dir / f"{path.stem}_darkir.png"
    to_pil_image(y[0].cpu()).save(destination)
    print(f"Saved {destination} | {time.time() - start:.2f}s")

print("INFERENCE COMPLETED")
