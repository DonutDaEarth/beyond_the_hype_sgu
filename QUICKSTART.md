# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 2: Choose Your Demo Format

#### Option A: Jupyter Notebook (Detailed Analysis)

```powershell
jupyter notebook demo_notebook.ipynb
```

Then run cells sequentially with `Shift+Enter`

#### Option B: Streamlit Web App (Live Presentation)

```powershell
streamlit run app.py
```

App opens automatically at http://localhost:8501

### Step 3: Explore!

## ⚡ What Each File Does

| File                      | Purpose                      | When to Use                            |
| ------------------------- | ---------------------------- | -------------------------------------- |
| `demo_notebook.ipynb`     | Interactive technical demo   | Deep dive, code review                 |
| `app.py`                  | Web-based visual demo        | Live presentation, audience engagement |
| `PRESENTATION_OUTLINE.md` | Complete presentation script | Preparation, rehearsal                 |
| `test_cases.json`         | Curated test examples        | Reference, extending tests             |
| `SETUP.md`                | Detailed setup instructions  | Troubleshooting                        |

## 🎯 For Your Presentation

**Before presenting:**

1. Run the notebook once to cache models (~2GB download)
2. Test the Streamlit app
3. Review `PRESENTATION_OUTLINE.md`

**During presentation:**

- Use Streamlit app for visual impact
- Fall back to notebook for technical details
- Have backup screenshots ready

## 📊 Key Demonstrations

1. **Basic Arithmetic** - Models fail at 347 + 589
2. **Financial Reporting** - Wrong numbers in summaries
3. **Consistency Test** - Different answers for same problem
4. **Medical Dosage** - Life-threatening errors
5. **Batch Analysis** - Overall <50% accuracy

## 🆘 Quick Troubleshooting

**Problem: Models downloading slowly**
→ First run downloads 2-3GB, be patient

**Problem: Out of memory**
→ Close other apps, restart kernel

**Problem: Import errors**
→ `pip install --upgrade transformers torch`

## 📚 Full Documentation

- Complete setup: See `SETUP.md`
- Presentation guide: See `PRESENTATION_OUTLINE.md`
- Project overview: See `README.md`

---

**Ready to expose the limitations of AI? Let's go! 🚀**
