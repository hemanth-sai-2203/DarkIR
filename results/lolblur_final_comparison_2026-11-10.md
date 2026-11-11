# LOL-Blur Final Restoration Comparison

Dataset: LOL-Blur test split
Number of images: 1,800
Evaluation date: 2026-11-10

## Results

| Model | PSNR | SSIM | LPIPS |
|---|---:|---:|---:|
| Pretrained DarkIR | 27.00246879 | 0.88291211 | 0.16201319 |
| Control 50k | 27.04574331 | 0.88117219 | 0.16642356 |
| Task-aware 50k | 26.97897587 | 0.87823065 | 0.15877382 |

## Training configurations

Common settings:
- Starting checkpoint: DarkIR_384.pt
- Training steps: 50,000
- Batch size: 2
- Crop size: 256
- Initial learning rate: 1e-5
- Learning rate schedule: cosine decay
- Random seed: 2026

Control:
- Objective: L1 restoration loss

Task-aware:
- Objective: L1 restoration loss + 0.1 task feature loss
- Task feature extractor: frozen Faster R-CNN ResNet-50 FPN

## Observations

- Control achieves the highest PSNR.
- Pretrained DarkIR achieves the highest SSIM.
- Task-aware achieves the lowest LPIPS.
- Task-aware does not improve all restoration metrics.
- Task-aware does not outperform control on ExDark validation detection.

## Evaluation logs

- results/lolblur_control_transformmatched_50000.log
- results/lolblur_task_transformmatched_50000.log

Note: LOL-Blur test results are part of the existing experimental history.
The test split was used in earlier experiments and is not an untouched holdout.
