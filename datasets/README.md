# Hugging Face Dataset Archive

This repository contains a script for downloading Hugging Face datasets and saving them to a specific folder. You can use the provided `download_dataset.py` script to download a specific dataset.

## Prerequisites

- Python 3.6 or higher
- The `datasets` library installed:

```bash
pip install datasets
```


## Usage

1. Navigate to the directory containing the `download_dataset.py` script.

2. Run the script by providing the dataset name as a command-line argument:


```bash
python download_dataset.py dataset-name
```

Replace `dataset-name` with the name of the Hugging Face dataset you want to download.

3. The dataset will be downloaded and saved in a folder named `./dataset-name` within the script's directory.

## Example

To download the `squad` dataset, run:

```bash
python download_dataset.py squad
```

The dataset will be saved in a folder named `./squad`.

