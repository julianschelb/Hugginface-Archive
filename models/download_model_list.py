from transformers import AutoModel, AutoTokenizer
import sys
import os


def download_model(model_name):
    """
    Download the specified Hugging Face model and tokenizer and save them to the given folder.

    Args:
        model_name (str): The name of the Hugging Face model to download.
        output_folder (str): The path to the folder where the model and tokenizer will be saved.
    """

    # Download the model and tokenizer
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Create a folder where you want to save the model and tokenizer files
    output_folder = "./" + model_name
    os.makedirs(output_folder, exist_ok=True)

    # Save the model and tokenizer to the specific folder
    model.save_pretrained(output_folder)
    tokenizer.save_pretrained(output_folder)


def process_text_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            model_name = line.strip()  # Remove leading/trailing whitespace and newlines
            download_model(model_name)
            print(f"Model and tokenizer for",
                  f"'{model_name}' have been saved.")


if __name__ == "__main__":

    # Replace with the actual path of your text file
    text_file_path = "./models.txt"
    process_text_file(text_file_path)
