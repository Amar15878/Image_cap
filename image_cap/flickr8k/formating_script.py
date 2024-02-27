def reformat_captions(input_filename, output_filename):
    """Reformats a captions file, adding ".jpg" to image IDs and a header.

    Args:
        input_filename: The name of the input captions file.
        output_filename: The name of the output file to create.
    """

    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        outfile.write("image,caption\n")  # Write the header

        for line in infile:
            if line.startswith("image"):  # Skip the original header
                continue
            image_id, caption = line.strip().split(" ", 1)
            outfile.write(f"{image_id}.jpg,{caption}\n")

if __name__ == "__main__":
    input_filename = "captions - Copy.txt"  # Your original file
    output_filename = "formatted_captions.txt"  # The reformatted output

    reformat_captions(input_filename, output_filename)
    print("Reformatting complete!")
