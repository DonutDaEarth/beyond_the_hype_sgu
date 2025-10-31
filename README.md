# Beyond the Hype: When Transformers Can't Count

## Project Thesis

**Common Understanding:**

> "Encoder-Decoder Transformers and their variants (like GPT, T5, RoBERTa) have revolutionized tasks like Machine Translation and Summarization, achieving near-human levels of performance."

**Our Counter-Thesis:**

> "Despite their linguistic sophistication, state-of-the-art Transformer models fail catastrophically at basic numerical reasoning tasks that any elementary school student could solve. This fundamental limitation poses serious risks for real-world applications involving financial data, scientific reporting, and quantitative analysis."

## The Critical Limitation: Numerical Reasoning Failure

### Hypothesis

We hypothesize that popular Transformer models (T5, BART, GPT-2) will:

1. **Fail to perform basic arithmetic** embedded in natural language contexts
2. **Generate confident but incorrect numerical summaries** when processing texts with quantitative information
3. **Produce inconsistent results** when the same numerical problem is rephrased
4. **Hallucinate plausible-sounding but factually wrong numbers** in summarization tasks

## Why This Matters

### Real-World Impact

- **Financial Reporting**: Automated news bots could report wrong stock prices, losses, or gains
- **Medical Records**: Summarization of patient data could misstate dosages or vital signs
- **Scientific Communication**: Research summaries might misrepresent experimental results
- **Legal Documents**: Contract analysis tools could miscalculate terms, dates, or amounts
- **Business Intelligence**: Executive summaries might contain incorrect KPIs and metrics

### The Deception

These models produce text that _looks_ professional and confident, making errors harder to detect without careful fact-checking.

## Project Components

### 1. Interactive Jupyter Notebook (`demo_notebook.ipynb`)

- Live demonstrations of model failures
- Side-by-side comparisons of input vs. output
- Multiple test cases across different scenarios

### 2. Streamlit Web Application (`app.py`)

- User-friendly interface for live demos
- Real-time model inference
- Visual comparison of results

### 3. Test Dataset (`test_cases.json`)

- Curated examples designed to expose failures
- Categories: arithmetic, counting, comparison, aggregation

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

# Or open the Jupyter notebook
jupyter notebook demo_notebook.ipynb
```

## Models Tested

- **T5-base**: Google's Text-to-Text Transfer Transformer
- **BART-large**: Facebook's denoising autoencoder for pretraining
- **GPT-2**: OpenAI's autoregressive language model

## Key Findings Preview

1. Models struggle with multi-step arithmetic (e.g., "If revenue was $100M and grew by 25%, what is the new revenue?")
2. Summarization models often change or omit numerical values
3. Small rephrasing of the same problem yields different (wrong) answers
4. Models show overconfidence bias - they don't indicate uncertainty

## Team Members

[Add your team members here]

## Presentation Structure

See `PRESENTATION_OUTLINE.md` for the complete 30-minute presentation flow.

---

_"The most dangerous kind of AI failure is the one that looks like success."_
