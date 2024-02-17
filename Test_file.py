from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenize = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length, num_beam = 16, 4
gen_kwargs = {"max_length": max_length, "num_beam": num_beam}


def predict_caption(image_paths):
    images = []
    for image_path in image_paths:
        j_image = Image.open(image_path)
        # convert the image to rgb
        #if j_image.mode != "RGB":
        #    j_image = j_image.convert(mode="RGB")
        #images.append(j_image)

    pixel_values = feature_extractor(images=images, return_tensor="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenize.batch_decode(output_ids, skip_special_tokens=True)
    # Updates the following
    preds = [preds.strip() for pred in preds]
    print("Final Caption is: ", preds)
    return preds


predict_caption(['surfing.jpeg'])