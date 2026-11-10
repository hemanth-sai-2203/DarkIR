# Qualitative LOL-Blur Comparison

Date: 2026-11-10
Samples: 6
Models: Pretrained DarkIR, Control 50k, Task-aware 50k

## Observations

1. All three models improve visibility compared with low-light inputs.
2. All three generally preserve scene structure and major details.
3. Pretrained and fine-tuned outputs are visually very similar.
4. No consistent visual advantage of task-aware training is apparent.
5. No obvious additional artifacts are observed in the selected examples.

## Interpretation

The qualitative comparison does not establish a clear visual
superiority of task-aware training. Its LPIPS improvement over
the control is supported numerically, but is not readily apparent
in these six examples.

The six examples are illustrative and do not replace full-dataset
quantitative evaluation.

Comparison image:
results/qualitative_lolblur_2026-11-10/comparison_grid.png
