# Setup and Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 8GB+ RAM (for running Transformer models)
- Internet connection (for first-time model downloads)

## Installation Steps

### 1. Clone or Navigate to the Project Directory

```powershell
cd "c:\Users\ss1ku\01 STEVEN FILES\SGU\7th Semester\Machine Learning\beyond_the_hype"
```

### 2. Create a Virtual Environment (Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

**Note:** First installation may take 10-15 minutes as it downloads PyTorch and Transformers libraries.

### 4. Verify Installation

```powershell
python -c "import transformers; import torch; print('✓ Installation successful!')"
```

## Running the Demonstration

### Option 1: Jupyter Notebook (Recommended for Deep Dive)

```powershell
# Start Jupyter
jupyter notebook

# Open 'demo_notebook.ipynb' in your browser
# Run cells sequentially (Shift+Enter)
```

**First-time setup:** The notebook will download pre-trained models (~1-2GB total):

- T5-base (~900MB)
- BART-large-cnn (~1.6GB)
- GPT-2 (~500MB)

This happens automatically on first run and is cached for future use.

### Option 2: Streamlit Web App (Best for Live Presentation)

```powershell
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

**App Features:**

- Interactive test categories
- Real-time model inference
- Visual result comparisons
- Batch analysis with charts

## Troubleshooting

### Issue: Models downloading slowly

**Solution:** First run will download ~2-3GB of model weights. Be patient or pre-download models:

```python
from transformers import T5ForConditionalGeneration, BartForConditionalGeneration
T5ForConditionalGeneration.from_pretrained('t5-base')
BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
```

### Issue: Out of Memory errors

**Solution:**

- Close other applications
- Use smaller batch sizes
- Restart Python kernel
- If persistent, use Google Colab (free GPU): Upload `demo_notebook.ipynb` to Colab

### Issue: Transformers version conflicts

**Solution:**

```powershell
pip install --upgrade transformers torch
```

### Issue: Streamlit not opening

**Solution:**

```powershell
# Manually open browser to:
# http://localhost:8501
```

## For Presentation Day

### Pre-Presentation Checklist

1. ✓ Run through entire notebook to cache models
2. ✓ Test Streamlit app launches properly
3. ✓ Verify internet connection (for model loading)
4. ✓ Close unnecessary applications to free RAM
5. ✓ Have backup: screenshots of expected results
6. ✓ Test on presentation computer if different from development machine

### Quick Start (Day of Presentation)

```powershell
# Navigate to project
cd "c:\Users\ss1ku\01 STEVEN FILES\SGU\7th Semester\Machine Learning\beyond_the_hype"

# Activate environment
.\venv\Scripts\Activate.ps1

# Option A: Jupyter Notebook
jupyter notebook demo_notebook.ipynb

# Option B: Streamlit App
streamlit run app.py
```

### Offline Mode (No Internet)

If models are already cached, everything works offline. Cache location:

- Windows: `C:\Users\[username]\.cache\huggingface\`

You can verify models are cached before going offline.

## File Structure

```
beyond_the_hype/
├── README.md                    # Project overview
├── SETUP.md                     # This file
├── PRESENTATION_OUTLINE.md      # Detailed presentation guide
├── requirements.txt             # Python dependencies
├── demo_notebook.ipynb          # Interactive Jupyter demonstration
├── app.py                       # Streamlit web application
└── venv/                        # Virtual environment (after setup)
```

## System Requirements

### Minimum:

- CPU: Dual-core 2.0GHz
- RAM: 8GB
- Storage: 5GB free space
- OS: Windows 10/11, macOS 10.14+, Linux

### Recommended:

- CPU: Quad-core 2.5GHz+
- RAM: 16GB
- Storage: 10GB free space
- GPU: NVIDIA GPU with CUDA support (optional, speeds up inference)

## Additional Notes

### GPU Acceleration (Optional)

If you have an NVIDIA GPU:

```powershell
# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Using Google Colab (Alternative)

If local machine is insufficient:

1. Go to https://colab.research.google.com
2. Upload `demo_notebook.ipynb`
3. Run cells (free GPU available)
4. Note: Streamlit app won't work in Colab

## Getting Help

### Resources:

- Hugging Face Docs: https://huggingface.co/docs/transformers
- Streamlit Docs: https://docs.streamlit.io
- PyTorch Docs: https://pytorch.org/docs

### Common Commands:

```powershell
# Update all packages
pip install --upgrade -r requirements.txt

# Check installed versions
pip list

# Clear cache (if needed)
pip cache purge

# Deactivate virtual environment
deactivate
```

## Contact

[Add team contact information here]

---

**You're all set! Good luck with your presentation! 🚀**
