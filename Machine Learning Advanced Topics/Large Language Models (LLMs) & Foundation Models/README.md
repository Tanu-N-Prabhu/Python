# Large Language Models (LLMs) & Foundation Models

_Educational Guide_

**Last Updated:** 2025-08-15

## Overview
Large Language Models (LLMs) like GPT, BERT, and LLaMA have transformed natural language processing. They are trained on vast datasets and can adapt to a wide range of tasks with minimal task-specific data.

**Foundation Models** are large pre-trained models that serve as a base for many downstream applications: NLP, vision, multi-modal AI, and more.

---

## Subtopics

### 1. Transformer Architectures
- **BERT**: Bidirectional encoder for understanding tasks like classification, question answering.
- **GPT**: Decoder-only architecture for generative tasks.
- **LLaMA**: Meta’s family of efficient LLMs optimized for research and deployment.
- **Why it matters**: Transformers are the backbone of modern LLMs. All major companies (Google PaLM, OpenAI GPT, Meta LLaMA) use them.

---

### 2. Parameter-Efficient Fine-Tuning (PEFT)
- **LoRA**: Fine-tune small matrices inside the model instead of all weights.
- **QLoRA**: LoRA + 4-bit quantization to drastically reduce memory usage.
- **PEFT**: A general term for techniques that adapt large models with minimal parameter changes.
- **Why it matters**: Saves compute and allows fine-tuning on a single GPU.

---

### 3. Prompt Engineering & In-Context Learning
- **Prompt Engineering**: Crafting effective inputs to guide model outputs.
- **In-Context Learning**: Providing examples within a prompt without updating model weights.
- **Why it matters**: Enables fast prototyping without fine-tuning.

---

### 4. Retrieval-Augmented Generation (RAG)
- Combines LLMs with a retrieval system (e.g., vector database).
- Injects external knowledge into the model at inference time.
- **Example**: Domain-specific QA where LLM retrieves relevant documents before answering.
- **Why it matters**: Keeps answers up-to-date without retraining.

---

## Why This Topic is Important
- Used in products like **Google PaLM**, **Microsoft Copilot**, **OpenAI GPT**, **Meta LLaMA**.
- Powers search engines, chat assistants, translation tools, and code generation systems.
- PEFT and RAG enable practical, efficient, and scalable use of LLMs in production.

---

## Project: Fine-Tune a GPT-like Model with LoRA/QLoRA
### Goal
Fine-tune a small GPT-like model on a custom dataset and deploy it via Hugging Face.

### Tools & Libraries
- `transformers`
- `datasets`
- `peft`
- `bitsandbytes` (for QLoRA)
- `accelerate`
- `huggingface_hub`

### Steps
1. **Install dependencies** in Colab.
2. **Load a GPT-like base model** (small enough for Colab).
3. **Prepare dataset** (custom or public).
4. **Apply LoRA/QLoRA** for efficient fine-tuning.
5. **Train** using PEFT.
6. **Evaluate** performance.
7. **Push to Hugging Face Hub** for easy sharing.

---

## Educational Notes
- Every step in the accompanying Colab notebook is annotated.
- Includes diagrams for Transformer architecture.
- Shows trade-offs between LoRA, QLoRA, and full fine-tuning.
- Demonstrates both training and prompt-engineering approaches.

---

## References
- [Attention is All You Need](https://arxiv.org/abs/1706.03762)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- [Hugging Face PEFT Docs](https://huggingface.co/docs/peft/index)
