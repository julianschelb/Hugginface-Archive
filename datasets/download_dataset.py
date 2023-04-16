import sys
import os
from datasets import load_dataset

def download_dataset(dataset_name, output_folder):
    """
    Download the specified Hugging Face dataset and save it to the given folder.

    Args:
        dataset_name (str): The name of the Hugging Face dataset to download.
        output_folder (str): The path to the folder where the dataset will be saved.
    """

    # Download the dataset
    dataset = load_dataset(dataset_name)
	
    # Create a folder where you want to save the dataset files
    output_folder = "./" + dataset_name
    os.makedirs(output_folder, exist_ok=True)

    # Save the dataset to the specified folder
    dataset.save_to_disk(output_folder)
    print(f"Dataset '{dataset_name}' has been saved to '{output_folder}'.")

def main():
    # Parse command-line arguments
    if len(sys.argv) > 1:
        dataset_name = sys.argv[1]
    else:
        print("Error: Please provide the dataset name as a command-line argument.")
        sys.exit(1)

    # Create a folder where you want to save the dataset files
    output_folder = "./" + dataset_name
    #os.makedirs(output_folder, exist_ok=True)

    # Download and save the dataset
    download_dataset(dataset_name, output_folder)
    #print(f"Dataset '{dataset_name}' has been saved to '{output_folder}'.")


if __name__ == "__main__":
    main()

