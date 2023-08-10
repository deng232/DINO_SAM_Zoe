# DINO_SAM_Zoe
example of piping grounding-segment-anything with ZoeDepth estimation


## setup
in your venv
```
python -m pip install -e .
```
## Preliminary Works
<div align='center'>
| Title | Intro | Description | Links |
|:----:|:----:|:----:|:----:|
| [Segment-Anything](https://arxiv.org/abs/2304.02643) | ![](https://github.com/facebookresearch/segment-anything/blob/main/assets/model_diagram.png?raw=true) | A strong foundation model aims to segment everything in an image, which needs prompts (as boxes/points/text) to generate masks | [[Github](https://github.com/facebookresearch/segment-anything)] <br> [[Page](https://segment-anything.com/)] <br> [[Demo](https://segment-anything.com/demo)] |
| [Grounding DINO](https://arxiv.org/abs/2303.05499) | ![](https://github.com/IDEA-Research/GroundingDINO/blob/main/.asset/hero_figure.png?raw=True) | A strong zero-shot detector which is capable of to generate high quality boxes and labels with free-form text. | [[Github](https://github.com/IDEA-Research/GroundingDINO)] <br> [[Demo](https://huggingface.co/spaces/ShilongLiu/Grounding_DINO_demo)] |
|[ZoeDepth](https://arxiv.org/abs/2302.12288) |![](https://raw.githubusercontent.com/isl-org/ZoeDepth/main/assets/zoedepth-teaser.png) | ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth| [[Demo](https://huggingface.co/spaces/shariqfarooq/ZoeDepth)]|
| [MiDas](https://arxiv.org/abs/1907.01341v3) | ![]() | Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer

</div>