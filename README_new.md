# 🤖 Beyond the Hype: When GPT-2 Hallucinates

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Transformers](https://img.shields.io/badge/🤗-Transformers-orange.svg)](https://huggingface.co/transformers/)

**A Machine Learning project demonstrating factual inaccuracies (hallucinations) in GPT-2's text generation**

---

## 📋 Project Overview

This project demonstrates a critical limitation of transformer-based language models: **factual hallucination**. While GPT-2 generates fluent and coherent text, it frequently produces plausible-sounding but factually incorrect or nonsensical information, making it unreliable for tasks requiring accuracy such as summarization, translation, and information retrieval.

### 🎯 Project Thesis

> _Despite GPT-2's impressive text generation capabilities, the model frequently generates plausible-sounding but factually incorrect information (hallucinations), making it unreliable for tasks requiring factual accuracy._

---

## 🔑 Key Limitation: Factual Inaccuracy (Hallucination)

**What is Hallucination?**

- AI-generated content that sounds plausible but is factually incorrect
- Includes invented facts, wrong dates, fabricated names, and nonsensical claims
- Occurs because the model predicts likely word sequences, NOT facts

**Why It Matters:**

- ❌ Unreliable for news summarization
- ❌ Dangerous for medical/legal/financial applications
- ❌ Spreads misinformation
- ❌ No uncertainty awareness (confident when wrong)

---

## 🧪 Demonstrations

This project includes multiple examples of GPT-2 hallucinations across different domains:

### 1. 📚 Historical Facts

- World War II dates
- Scientific discoveries
- Famous historical figures

### 2. 🌍 Geographic Information

- Country capitals
- Mountain locations
- Geographic features

### 3. 📰 News Summarization

- Battery technology research
- Medical trials
- **Risk:** Changes numbers, invents quotes, adds false details

### 4. ❓ Question Answering

- Basic factual questions
- Company information
- **Risk:** Provides confident but incorrect answers

### 5. 🔬 Technical Explanations

- Scientific concepts
- Literary references
- **Risk:** Invents capabilities and fabricates context

---

## 🤖 Model Analyzed

**GPT-2 (OpenAI, 2019)**

- Parameters: 117 million
- Architecture: Transformer decoder-only
- Training: Autoregressive language modeling
- **Limitation:** Frequently hallucinates factual information

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- 4GB+ RAM
- Internet connection (for model download)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/beyond_the_hype.git
cd beyond_the_hype
```

2. **Create and activate virtual environment:**

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### Requirements

```
transformers==4.35.0
torch==2.1.0
pandas==2.1.3
matplotlib==3.8.2
seaborn==0.13.0
streamlit==1.29.0
numpy==1.26.2
```

---

## 💻 Usage

### Option 1: Jupyter Notebook (Detailed Analysis)

1. **Start Jupyter:**

```bash
jupyter notebook
```

2. **Open and run:**

```
demo_notebook_new.ipynb
```

**Features:**

- 10+ hallucination test cases
- Ground truth comparisons
- Quantitative analysis
- Consistency testing
- Visualizations

### Option 2: Streamlit App (Interactive Demo)

1. **Run the app:**

```bash
streamlit run app_new.py
```

2. **Access in browser:**

```
http://localhost:8501
```

**Features:**

- Interactive hallucination tests
- Multiple test categories
- Real-time generation
- Custom prompt testing
- Visual comparisons

---

## 📊 Key Findings

### Main Observations:

1. **High Hallucination Rate:** GPT-2 frequently generates factually incorrect information across all tested domains
2. **Plausible Fluency:** Generated text sounds convincing but lacks factual grounding
3. **No Uncertainty:** Model shows same confidence for correct and incorrect outputs
4. **Inconsistency:** Same prompt produces different (often wrong) results

### Example Hallucinations:

- ❌ Incorrect historical dates
- ❌ Fabricated geographic facts
- ❌ Invented company information
- ❌ Changed numbers in summaries
- ❌ False scientific claims

---

## 🎓 Educational Value

This project is ideal for:

- **Students:** Understanding AI limitations
- **Developers:** Learning about model reliability
- **Researchers:** Analyzing hallucination patterns
- **General Public:** AI literacy and awareness

**Use Cases:**

- Machine Learning course projects
- AI ethics discussions
- Technical presentations (30-minute demo)
- Research on factual accuracy in LLMs

---

## 📁 Project Structure

```
beyond_the_hype/
│
├── demo_notebook_new.ipynb    # Jupyter notebook with analysis
├── app_new.py                 # Streamlit interactive app
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
└── (old files - archived)
    ├── demo_notebook.ipynb    # Original 5-model version
    └── app.py                 # Original multi-model app
```

---

## 🔬 Technical Details

### Model Loading

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
```

### Text Generation

```python
def generate_gpt2_text(prompt, max_length=200, temperature=0.8):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Hallucination Detection

The project uses **ground truth comparison** to identify:

- Factual errors
- Invented details
- Changed numbers/dates
- Fabricated names/quotes

---

## ⚠️ Limitations & Warnings

### Model Limitations:

- **Not a fact-checker:** GPT-2 doesn't verify information
- **No knowledge base:** Predicts words, not facts
- **Training data cutoff:** Knowledge limited to training data (2019)
- **Bias propagation:** May reflect biases in training data

### Usage Warnings:

- ⚠️ **Never use GPT-2 for critical applications** (medical, legal, financial)
- ⚠️ **Always verify AI-generated content**
- ⚠️ **Don't rely on it for factual information**
- ⚠️ **Educate users about hallucination risks**

---

## 🎯 Future Improvements

Potential enhancements:

1. **Retrieval-Augmented Generation (RAG):** Combine with search engines
2. **Fact verification systems:** External knowledge base integration
3. **Uncertainty quantification:** Confidence scores
4. **Fine-tuning experiments:** Domain-specific accuracy
5. **Comparison with newer models:** GPT-3.5, GPT-4, Claude
6. **Automated hallucination detection:** ML-based fact-checking

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- Additional test cases
- New hallucination categories
- Visualization enhancements
- Documentation improvements
- Performance optimizations

**To contribute:**

1. Fork the repository
2. Create feature branch: `git checkout -b feature/NewTest`
3. Commit changes: `git commit -m 'Add new hallucination test'`
4. Push to branch: `git push origin feature/NewTest`
5. Submit pull request

---

## 📚 References

### Papers:

- Radford et al. (2019) - "Language Models are Unsupervised Multitask Learners"
- Ji et al. (2023) - "Survey of Hallucination in Natural Language Generation"
- Maynez et al. (2020) - "On Faithfulness and Factuality in Abstractive Summarization"

### Resources:

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OpenAI GPT-2 Blog](https://openai.com/research/better-language-models)
- [AI Hallucination Research](https://arxiv.org/abs/2202.03629)

---

## 📧 Contact

**Project Author:** [Your Name]

- **University:** SGU (Swiss German University)
- **Course:** Machine Learning (7th Semester)
- **Email:** your.email@example.com
- **GitHub:** [@yourusername](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI** for GPT-2 model
- **Hugging Face** for Transformers library
- **Streamlit** for interactive web framework
- **SGU Machine Learning Course** for project opportunity

---

## ⭐ Star History

If you find this project useful for understanding AI limitations, please consider giving it a star! ⭐

---

<div align="center">

**🚨 CRITICAL REMINDER 🚨**

_GPT-2 is a powerful text generator but is NOT a reliable source of factual information. Always verify AI-generated content, especially in contexts where accuracy matters._

**This project aims to increase awareness about AI hallucination risks.**

</div>
