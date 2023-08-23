import supervision as sv
import os
import torch
import cv2
import numpy as np
from segment_anything import SamPredictor, SamAutomaticMaskGenerator, sam_model_registry
from groundingdino.util.inference import Model
from zoedepth.utils.config import get_config
from zoedepth.models.builder import build_model



DINO_CONFIG_PATH = os.path.join(
    os.getcwd(), "groundingdino/config/GroundingDINO_SwinT_OGC.py")
print(DINO_CONFIG_PATH, "; exist:", os.path.isfile(DINO_CONFIG_PATH))
DINO_WEIGHTS_NAME = "groundingdino_swint_ogc.pth"
DINO_WEIGHTS_PATH = os.path.join(os.getcwd(), "weights", DINO_WEIGHTS_NAME)
SAM_WEIGHTS_NAME = "sam_vit_h_4b8939.pth"
SAM_WEIGHTS_PATH = os.path.join(os.getcwd(), "weights", SAM_WEIGHTS_NAME)
print(SAM_WEIGHTS_PATH, "; exist:", os.path.isfile(SAM_WEIGHTS_PATH))

image = cv2.imread( os.path.join(os.getcwd(),'testinput','DSC02586.JPG'))
DINO_model = Model(model_config_path=DINO_CONFIG_PATH,
                   model_checkpoint_path=DINO_WEIGHTS_PATH)

sam_predictor = SamPredictor(sam_model_registry['vit_h'](
    checkpoint=SAM_WEIGHTS_PATH).to(device=torch.device('cuda')))

model_zoe_nk = build_model(get_config("zoedepth_nk", "infer"))
model_zoe_nk.to(torch.device('cuda'))

sam_predictor.set_image(image)
detections = DINO_model.predict_with_caption(
    image=image, caption='all duck', box_threshold=.55, text_threshold=.25)
detections[0].mask = [masks[np.argmax(scores)] for masks, scores, _ in map(
    lambda box: sam_predictor.predict(box=box, multimask_output=True), detections[0].xyxy)]

depth_map = model_zoe_nk.infer_pil(image, output_type="numpy")

#depth_map = model_zoe_nk.infer_pil(image, output_type="numpy")
depth_map = model_zoe_nk.infer_pil(image, output_type="numpy",pad_input=False) # "pad_input = False" increase accuracy

box_annotator = sv.BoxAnnotator(text_scale=1.5)
mask_annotator = sv.MaskAnnotator()
annotated_image = mask_annotator.annotate(
    scene=image, detections=detections[0])
annotated_image = box_annotator.annotate(scene=annotated_image, detections=detections[0], labels=[
                                         f"{confidence:.4f} {name} {average_depth:.4f}" for confidence, name, average_depth in
                                         zip(detections[0].confidence.tolist(), detections[1],
                                             [sum(mask)/len(mask) for mask in masklist])])


os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
sv.plot_image(annotated_image, (16, 16))

