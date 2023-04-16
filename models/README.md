# Hugging Face Model Archive

This repository is an archive of Hugging Face models. It provides a simple script to download any Hugging Face model and its tokenizer using the Transformers library.

## Prerequisites

Before you can use the script, make sure you have the following installed:

- Python 3.6 or later
- Transformers library

You can install the Transformers library using pip:

```bash
pip install transformers
```


## Usage

1. Navigate to the directory containing the `download_model.py` script.

2. Run the script by providing the model name as a command-line argument:


```bash
python download_model.py model-name
```

Replace `model-name` with the name of the Hugging Face model you want to download.

For example, to download the `distilbert-base-uncased` model, run:

```bash
python download_model.py distilbert-base-uncased
```

The model and tokenizer will be saved in a folder named `./distilbert-base-uncased`.

