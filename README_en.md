# ThinkRAG

[English](./README_en.md) | [简体中文](./README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Support: Ollama](https://img.shields.io/badge/Support-Ollama-green.svg)](https://ollama.com/)
[![Support: LlamaIndex](https://img.shields.io/badge/Support-LlamaIndex-purple.svg)](https://www.llamaindex.ai/)

---

## Table of Contents
- 🤔 [Overview](#overview)
- ✨ [Features](#features)
- 🧸 [Model Support](#model-support)
- 🛫 [Quick Start](#quick-start)
- 📖 [User Guide](#user-guide)
- 🔬 [Architecture](#architecture)
- 📜 [Roadmap](#roadmap)
- 📄 [License](#license)

---

## Overview

ThinkRAG is a Retrieval-Augmented Generation (RAG) system powered by Large Language Models (LLMs). It can be easily deployed on a laptop to implement Q&A functionalities with a local knowledge base.

This system is built using LlamaIndex and Streamlit, optimized for both English and Chinese users. It supports various LLM service providers, including **Ollama's Gemma model**, ensuring flexibility and robustness in information retrieval and response generation.

---

## Features

ThinkRAG is designed for professionals, researchers, students, and other knowledge workers. Key features include:

- **Complete LlamaIndex Framework Integration**:
  Utilizes the full capabilities of LlamaIndex for efficient data handling and retrieval.
- **Local File Storage**:
  No need for external databases, enhancing data privacy and control.
- **No GPU Required**:
  Optimized to run on standard laptops.
- **Local and Remote Model Support**:
  Seamlessly integrates locally deployed models via Ollama and supports remote APIs like OpenAI, Zhipu, Moonshot, and DeepSeek.
- **Chinese Language Optimization**:
  - Uses Spacy Text Splitter for better handling of Chinese characters.
  - Employs Chinese Title Enhancement features.
  - Utilizes Bilingual Embedding Models (e.g., BAAI's `bge-large-zh-v1.5`).

---

## Model Support

ThinkRAG supports a wide range of models through various LLM providers integrated with the LlamaIndex data framework.

### Ollama
- **Local Deployment**: Runs models locally, ensuring data privacy.
- **Supported Models**: Gemma (`gemma:2b`), Llama, GLM, Mistral, Phi, Llava, etc.
- **Installation**: Models can be installed via the Ollama CLI.
- **Documentation**: Visit the [Ollama Official Website](https://ollama.com/) for more details.

### OpenAI
- **API Access**: Supports models like `gpt-4`, `gpt-3.5`, and `gpt-4o`.
- **Setup**: Requires an OpenAI API key.

### Zhipu, Moonshot, DeepSeek
- ThinkRAG integrates with APIs from Zhipu, Moonshot, and DeepSeek for additional model options.

### Embedding and Reranking Models
- **Embedding Models**: BAAI's `bge-large-zh-v1.5` and `bge-small-zh-v1.5`.
- **Reranking Models**: BAAI's `bge-reranker-base` and `bge-reranker-large`.

---

## Quick Start

### Step 1: Clone the Repository
	git clone https://github.com/CodeQueenie/ThinkRAG_.git

#### Locate Directory
	cd ThinkRAG_


### Step 2: Set Up a Virtual Environment
	python -m venv venv

### Activate the virtual environment:
#### Windows:
	venv\Scripts\activate
#### macOS/Linux:
	source venv/bin/activate

### Step 3: Install Dependencies
	python -m pip install --upgrade pip setuptools wheel pip install -r requirements.txt


### Step 4: Install and Configure Ollama
#### 1. Download and Install Ollama: Visit the Ollama Official Website: https://ollama.com/ for installation instructions.

#### 2. Install the Gemma Model:
	ollama pull gemma:2b


#### 3. Verify Installation:
	ollama list

Ensure `gemma:2b` is listed among the installed models.

### Step 5: Run the Application
#### Run the following command:
	streamlit run app.py

This will open the application in your default browser at http://localhost:8501.

---

## User Guide

### System Configuration
ThinkRAG allows configuration of LLM models and parameters directly through the interface.

- **Model Selection**: Choose a model (e.g., Gemma or OpenAI GPT) from the interface.
- **API Keys**: Enter API keys for selected providers.
- **Advanced Settings**: Adjust temperature, top-k, response mode, and more.

### Knowledge Base Management
- **Upload Documents**: Add PDFs, DOCX, or PPTX files.
- **Web Content**: Paste URLs to fetch and save web content.
- **Manage Documents**: View, delete, or update saved knowledge base documents.

### Query
Interact with the knowledge base using natural language queries.

---

## Architecture

ThinkRAG uses the following components:

| Mode         | Development | Production |
|--------------|-------------|------------|
| RAG Framework| LlamaIndex  | LlamaIndex |
| Frontend     | Streamlit   | Streamlit  |
| Storage      | SimpleDocumentStore | Redis |

For a full architecture overview, refer to the documentation.

---

## Roadmap

Planned features include:

- Multimodal knowledge bases.
- Knowledge graph integration.
- Advanced user interfaces with Electron or React.

---

## License

This project is licensed under the MIT License.








   

