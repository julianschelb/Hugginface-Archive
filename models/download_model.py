from transformers import AutoModel, AutoTokenizer
import sys
import os


def download_model(model_name, output_folder):
    """
    Download the specified Hugging Face model and tokenizer and save them to the given folder.

    Args:
        model_name (str): The name of the Hugging Face model to download.
        output_folder (str): The path to the folder where the model and tokenizer will be saved.
    """

    # Download the model and tokenizer
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Save the model and tokenizer to the specific folder
    model.save_pretrained(output_folder)
    tokenizer.save_pretrained(output_folder)


if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        model_name = "gpt2"

    # Create a folder where you want to save the model and tokenizer files
    output_folder = "./" + model_name
    os.makedirs(output_folder, exist_ok=True)

    # Download and save the model and tokenizer
    download_model(model_name, output_folder)
    print(f"Model and tokenizer for '{model_name}' have been saved to '{output_folder}'.")

