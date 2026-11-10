# Final Experimental Results
Date: 2026-11-10
Project: Task-Aware Low-Light Image Restoration

## 1. LOL-Blur Restoration

Test images: 1800

| Model | PSNR | SSIM | LPIPS |
|---|---:|---:|---:|
| Pretrained DarkIR | 27.00246879 | 0.88291211 | 0.16201319 |
| Control 50k | 27.04574331 | 0.88117219 | 0.16642356 |
| Task-aware 50k | 26.97897587 | 0.87823065 | 0.15877382 |

Control obtains the highest PSNR.
Pretrained obtains the highest SSIM.
Task-aware obtains the lowest LPIPS.

## 2. ExDark Validation

Images: 1800

| Model | mAP@50 | mAP@50:95 |
|---|---:|---:|
| Original low-light | 0.5873 | 0.2795 |
| Pretrained DarkIR | 0.5510 | 0.2628 |
| Control 50k | 0.5531 | 0.2637 |
| Task-aware 50k | 0.5517 | 0.2623 |

## 3. ExDark Independent Test

Images: 2563
Ground-truth boxes: 7117
Classes: 12

| Condition | mAP@50 | mAP@50:95 | mAP@75 |
|---|---:|---:|---:|
| Original low-light | 0.5836 | 0.2795 | 0.2308 |
| Pretrained DarkIR | 0.5355 | 0.2497 | 0.1986 |
| Control 50k | 0.5361 | 0.2505 | 0.2012 |
| Task-aware 50k | 0.5341 | 0.2494 | 0.1990 |

Detector: Frozen torchvision Faster R-CNN ResNet-50 FPN,
pretrained on COCO and evaluated zero-shot on ExDark.
Metrics computed using pycocotools COCOeval.

## 4. Interpretation

- Fine-tuning provides no consistent improvement across restoration metrics.
- Task-aware training gives the best LPIPS but lower PSNR and SSIM.
- Task-aware training does not improve object detection over control.
- Original low-light images achieve the highest ExDark test detection scores.
- Restoration quality and downstream detection performance are not
  necessarily aligned.

## 5. Limitations

- LOL-Blur test data was reused during earlier experimental iterations.
  It is not an untouched holdout.
- ExDark detector evaluation is zero-shot using a COCO-pretrained detector,
  not an ExDark-trained detector benchmark.
- Adaptive feature modulation from the initial proposal was not implemented.
- The implemented task-aware objective uses L1 restoration loss plus
  normalized cosine FPN feature consistency.

## 6. Reproducibility Files

- results/exdark_test_cocoeval_50000.json
- results/exdark_test_cocoeval_50000_predictions.json
- results/exdark_test_cocoeval_50000.log
- results/lolblur_final_comparison_2026-11-10.md
- results/qualitative_observations_2026-11-10.md
- results/qualitative_lolblur_2026-11-10/comparison_grid.png
