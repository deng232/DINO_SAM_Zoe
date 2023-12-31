
# DINO_SAM_Zoe
example of piping grounding-segment-anything with ZoeDepth estimation
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deng232/DINO_SAM_Zoe/blob/main/DINO_SAM_Zoe.ipynb)
colab example use the original repose from https://github.com/IDEA-Research/Grounded-Segment-Anything/tree/main

## setup
in your venv
```
python -m pip install -e .
```
create folder 'testinput' and 'weights', adding image and models(groundingdino_swint_ogc.pth, sam_vit_h_4b8939.pth,ZoeD_M12NK.pt) then the running the 'segdepth.py' shall showing the masked segmentation with annoattion of confidence level, name and depth( depth in this example is calculated by average of the depth map pixels in the masked region)
## Preliminary Works
## Preliminary Works

| Title | Intro | Description | Links |
|:-----:|:-----:|:-----------:|:-----:|
| [Segment-Anything](https://arxiv.org/abs/2304.02643) | ![Segment-Anything](https://github.com/facebookresearch/segment-anything/blob/main/assets/model_diagram.png?raw=true) | A strong foundation model aims to segment everything in an image, which needs prompts (as boxes/points/text) to generate masks | [Github](https://github.com/facebookresearch/segment-anything) <br> [Page](https://segment-anything.com/) <br> [Demo](https://segment-anything.com/demo) |
| [Grounding DINO](https://arxiv.org/abs/2303.05499) | ![Grounding DINO](https://github.com/IDEA-Research/GroundingDINO/blob/main/.asset/hero_figure.png?raw=true) | A strong zero-shot detector which is capable of generating high-quality boxes and labels with free-form text. | [Github](https://github.com/IDEA-Research/GroundingDINO) <br> [Demo](https://huggingface.co/spaces/ShilongLiu/Grounding_DINO_demo) |
| [ZoeDepth](https://arxiv.org/abs/2302.12288) | ![ZoeDepth](https://raw.githubusercontent.com/isl-org/ZoeDepth/main/assets/zoedepth-teaser.png) | ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth | [Demo](https://huggingface.co/spaces/shariqfarooq/ZoeDepth) |
| [MiDas](https://arxiv.org/abs/1907.01341v3) | ![MiDas]() | Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer | - |


