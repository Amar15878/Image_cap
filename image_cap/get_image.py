import os
from PIL import Image
from difflib import SequenceMatcher  # For approximate string matching

def load_data(captions_file, images_dir):
    """Loads image captions and creates a searchable mapping.
    Args: captions_file: Path to the captions CSV file. images_dir: Path to the directory containing the images.
    Returns: A dictionary mapping image IDs to their corresponding captions.
    """

    data = {}
    with open(captions_file, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            image_id, caption = line.strip().split(',', 1)
            data[image_id] = caption
    return data

def find_best_match(data, user_query):
    """Finds the best-matching image caption for the given user query.
    Args: data: The dictionary mapping image IDs to captions. user_query: The search query provided by the user.

    Returns: A tuple containing:
            - The image ID of the best match.
            - The corresponding caption.
            - The similarity ratio (how close the match is).
    """

    best_match_id = None
    best_match_caption = None
    best_match_ratio = 0.0

    for image_id, caption in data.items():
        similarity_ratio = SequenceMatcher(None, user_query, caption).ratio()
        if similarity_ratio > best_match_ratio:
            best_match_id = image_id
            best_match_caption = caption
            best_match_ratio = similarity_ratio

    return best_match_id, best_match_caption, best_match_ratio

def main():
    captions_file = "formatted_captions.txt"
    images_dir = "imagess"
    data = load_data(captions_file, images_dir)

    while True:
        user_query = input("Enter your image search query (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break

        image_id, caption, similarity_ratio = find_best_match(data, user_query)

        if image_id:
            image_path = os.path.join(images_dir, image_id)
            Image.open(image_path).show()
            print(f"Best Match: {caption} (Similarity: {similarity_ratio:.2f})")
        else:
            print("No matching images found.")

if __name__ == "__main__":
    main()