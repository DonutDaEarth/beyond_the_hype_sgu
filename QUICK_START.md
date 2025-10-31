# 🚀 Quick Start Guide: Running Your Demos

## Option 1: Jupyter Notebook Demo

### Step 1: Activate Environment

```bash
cd "c:\Users\ss1ku\01 STEVEN FILES\SGU\7th Semester\Machine Learning\beyond_the_hype"
venv\Scripts\activate
```

### Step 2: Launch Jupyter

```bash
jupyter notebook
```

### Step 3: Open Notebook

- Click on `demo_notebook_new.ipynb`
- Run all cells: `Cell` → `Run All`

### Expected Runtime

- **Setup cells:** ~30 seconds (import libraries)
- **Model loading:** ~15 seconds (download GPT-2 first time)
- **Each demo cell:** ~3-5 seconds per generation

---

## Option 2: Streamlit Interactive App

### Step 1: Activate Environment

```bash
cd "c:\Users\ss1ku\01 STEVEN FILES\SGU\7th Semester\Machine Learning\beyond_the_hype"
venv\Scripts\activate
```

### Step 2: Run Streamlit

```bash
streamlit run app_new.py
```

### Step 3: Open Browser

- Automatically opens: `http://localhost:8501`
- Or manually navigate to that URL

### App Features

- **6 tabs:** Historical, Geography, News, Q&A, Technical, Custom
- **Generate buttons:** Click to run each test
- **Settings sidebar:** Adjust temperature and max length
- **Custom test tab:** Try your own prompts!

---

## 🎯 During Your Presentation

### Recommended Flow

**Option A: Start with Streamlit (Recommended)**

1. Have Streamlit app already running before presentation
2. Walk through tabs in order
3. Generate 1-2 examples per category
4. Switch to Jupyter for quantitative analysis
5. Return to Streamlit for custom interactive demo

**Option B: Jupyter Only**

1. Run notebook before presentation
2. Scroll through pre-generated results
3. Re-run specific cells for live demo
4. Show visualizations and analysis

**Option C: Both (Most Impressive)**

1. Start with Jupyter for introduction and background
2. Switch to Streamlit for interactive demos
3. Return to Jupyter for analysis and visualizations
4. Finish with Streamlit custom test (audience participation)

---

## 🛠️ Troubleshooting

### Problem: Model won't load

**Error:** `OSError: Can't load tokenizer`

**Solution:**

```bash
# Clear cache and re-download
rm -rf ~/.cache/huggingface/
# Then restart notebook/app
```

### Problem: Streamlit won't start

**Error:** `streamlit: command not found`

**Solution:**

```bash
# Ensure virtual environment is activated
venv\Scripts\activate
# Reinstall streamlit
pip install streamlit
```

### Problem: Slow generation

**Issue:** Takes >10 seconds per generation

**Solution:**

```python
# In both notebook and app, reduce max_length
max_length=100  # Instead of 200
```

### Problem: Import errors

**Error:** `ModuleNotFoundError: No module named 'transformers'`

**Solution:**

```bash
pip install -r requirements.txt
```

---

## 📊 Presentation Checklist

### Before Starting:

- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] Streamlit app running (if using)
- [ ] Jupyter notebook cells executed (if using)
- [ ] Internet connected (first time model download)
- [ ] Browser ready

### During Presentation:

- [ ] Screen sharing on
- [ ] Notifications silenced
- [ ] Backup screenshots ready
- [ ] Timer visible
- [ ] Water nearby

### Test These Before Live Demo:

- [ ] Click "Generate" button works
- [ ] Output displays correctly
- [ ] Tabs switch smoothly
- [ ] Custom test accepts input
- [ ] Notebook cells run without errors

---

## 💡 Pro Tips

### Speed Up Demos

1. **Pre-generate examples** in Jupyter before presentation
2. **Keep Streamlit running** in background
3. **Use lower temperature** (0.5-0.7) for faster generation
4. **Reduce max_length** to 80-120 tokens

### Make It Interactive

1. **Ask audience for prompts** in Custom Test tab
2. **Let them predict** what GPT-2 will say
3. **Compare their guesses** to actual output
4. **Highlight specific hallucinations** with mouse pointer

### Handle Technical Issues

1. **Have screenshots** as backup
2. **Can narrate** pre-generated results
3. **Jupyter as fallback** if Streamlit crashes
4. **Keep calm** and explain the concept anyway

---

## 🎬 30-Minute Demo Schedule

**Minute 0-3:** Introduction

- Open Streamlit app homepage
- Show model info in sidebar

**Minute 3-7:** Background

- Switch to Jupyter notebook
- Show model loading cell output
- Explain helper functions briefly

**Minute 7-10:** Historical Facts Demo

- Streamlit: Historical Facts tab
- Generate WWII test
- Generate Einstein test
- Point out hallucinations

**Minute 10-13:** Geography Demo

- Streamlit: Geography tab
- Generate Australia capital
- Generate Mount Everest
- Highlight errors

**Minute 13-16:** News Summary Demo

- Streamlit: News Summary tab
- Read original article
- Generate summary
- Compare differences

**Minute 16-19:** Q&A Demo

- Streamlit: Q&A tab
- Generate continents question
- Generate Microsoft question
- Show confident incorrectness

**Minute 19-22:** Custom Interactive

- Streamlit: Custom Test tab
- Ask audience for prompt
- Generate together
- Identify hallucinations

**Minute 22-26:** Analysis

- Switch to Jupyter notebook
- Scroll to quantitative analysis
- Show consistency test results
- Display visualization

**Minute 26-30:** Conclusions

- Streamlit: Scroll to footer
- Read key takeaways
- Answer questions

---

## 📁 File Reference

### New Files (Use These!)

- `demo_notebook_new.ipynb` - Complete hallucination demo
- `app_new.py` - Streamlit interactive app
- `README_new.md` - Updated documentation
- `PRESENTATION_GUIDE.md` - This guide

### Old Files (Archive/Delete)

- `demo_notebook.ipynb` - Original 5-model version
- `app.py` - Original multi-model app
- `README.md` - Old documentation

---

## ⚡ Quick Commands Reference

### Windows PowerShell

**Activate environment:**

```powershell
venv\Scripts\activate
```

**Run Jupyter:**

```powershell
jupyter notebook
```

**Run Streamlit:**

```powershell
streamlit run app_new.py
```

**Install dependencies:**

```powershell
pip install -r requirements.txt
```

**Deactivate environment:**

```powershell
deactivate
```

---

## 🎯 Success Indicators

### ✅ Everything is working if:

- Streamlit app loads in <10 seconds
- Generate buttons produce text in <5 seconds
- All tabs are accessible
- Jupyter cells run without errors
- Visualizations display correctly
- Custom test accepts input

### ❌ Something is wrong if:

- Errors appear when clicking Generate
- App takes >30 seconds to start
- "Model not found" errors
- Blank outputs
- Cells throw exceptions

**Solution:** Check environment activation and reinstall dependencies

---

## 📞 Quick Help

### If stuck during presentation:

**Option 1:** Skip to backup screenshots

**Option 2:** Switch to Jupyter if Streamlit fails

**Option 3:** Explain the concept verbally with slides

**Option 4:** Show pre-generated results

**Remember:** The audience cares about the concept (hallucination), not perfect tech execution!

---

## 🎉 Final Checklist

**Ready to present when:**

- [ ] Can run Streamlit app successfully
- [ ] Can generate text in all tabs
- [ ] Jupyter notebook runs completely
- [ ] Understand each demo's purpose
- [ ] Can explain hallucination clearly
- [ ] Have backup plan ready
- [ ] Feeling confident!

**You've got this! Good luck! 🚀**
