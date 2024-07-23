# Langchain + ChatGPT

### Before we begin
```bash
python -V
mkdir pdf-chatbot cd pdf-chatbot
python -m venv env
source env/bin/activate
pip install langchain openai chromadb pymupdf tiktoken
```


A demo on how to build presentations using Slides.
```python
import os
from langchain.document_loaders import PyMuPDFLoader

os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'

loader = PyMuPDFLoader("./docs/example.pdf")
documents = loader.load()
```

---

## Formatting

You can use regular Markdown formatting, like *emphasized* and **bold** text.
1. Splitting the text into small, semantically meaningful chunks, often based on sentence boundaries.
2. Combining these small chunks into larger chunks until a specific size is reached, determined by a predefined function that measures the chunk size.
3. Once the chunk reaches the desired size, it becomes its own separate piece of text. A new chunk is then created with some overlap to maintain context between the chunks.

Text splitters allow customization along two axes:

1. How the text is split: This involves selecting a strategy for splitting the text, such as using sentence boundaries, paragraph breaks, or other semantic cues.
2. How the chunk size is measured: This refers to the function used to determine the size of the chunks, which could be based on the number of characters, words, sentences, or any other suitable metric.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)
```


---

## Slides

Use `---` to separate slides.