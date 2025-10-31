"""
Beyond the Hype: When GPT-2 Hallucinates
Streamlit Interactive Demo

Demonstrates how GPT-2 generates plausible but factually incorrect information
"""

import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="When GPT-2 Hallucinates",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 48px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .sub-header {
        font-size: 24px;
        color: #34495e;
        margin: 20px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        color: #856404;
        padding: 20px;
        border-left: 5px solid #ffc107;
        border-radius: 5px;
        margin: 15px 0;
    }
    .truth-box {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-left: 5px solid #28a745;
        border-radius: 5px;
        margin: 10px 0;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-left: 5px solid #dc3545;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load GPT-2 model"""
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    model.eval()
    return model, tokenizer

def generate_gpt2_text(model, tokenizer, prompt, max_length=200, temperature=0.8):
    """Generate text using GPT-2"""
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            temperature=temperature,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🤖 Beyond the Hype: When GPT-2 Hallucinates</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Project Goal
    Demonstrate how **GPT-2** generates plausible-sounding but **factually incorrect information** (hallucinations),
    making it unreliable for tasks requiring factual accuracy.
    
    **Key Finding:** GPT-2 predicts likely word sequences based on patterns, NOT facts!
    """)
    
    # Load model
    with st.spinner("Loading GPT-2 model..."):
        model, tokenizer = load_model()
    
    st.success("✓ GPT-2 model loaded successfully!")
    
    # Sidebar
    st.sidebar.title("⚙️ Settings")
    st.sidebar.markdown("---")
    
    temperature = st.sidebar.slider(
        "Temperature (higher = more random)",
        min_value=0.1,
        max_value=1.5,
        value=0.8,
        step=0.1
    )
    
    max_length = st.sidebar.slider(
        "Max output length",
        min_value=50,
        max_value=300,
        value=150,
        step=25
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### 📊 Model Info
    - **Model:** GPT-2 (117M params)
    - **Developer:** OpenAI (2019)
    - **Architecture:** Transformer decoder
    - **Limitation:** Factual hallucination
    """)
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📚 Historical Facts",
        "🌍 Geography",
        "📰 News Summary",
        "❓ Q&A",
        "🔬 Technical",
        "🎨 Custom Test"
    ])
    
    # Tab 1: Historical Facts
    with tab1:
        st.markdown("## 📚 Historical Facts Hallucination")
        st.markdown("**Risk:** GPT-2 will confidently state incorrect dates, names, and events.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Test 1: World War II")
            if st.button("Generate", key="hist1"):
                prompt = "World War II ended in"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">World War II ended in 1945 (May 8 in Europe, September 2 in the Pacific)</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
                
                st.markdown("**🚨 Check for:**")
                st.markdown('<div class="warning-box">• Incorrect year<br>• Invented battles<br>• Wrong historical figures<br>• Fabricated details</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Test 2: Einstein's Discovery")
            if st.button("Generate", key="hist2"):
                prompt = "Albert Einstein discovered the theory of relativity in"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">Special relativity: 1905, General relativity: 1915</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
                
                st.markdown("**🚨 Check for:**")
                st.markdown('<div class="warning-box">• Wrong year<br>• Invented collaborators<br>• Fabricated discovery details<br>• Incorrect scientific claims</div>', unsafe_allow_html=True)
    
    # Tab 2: Geography
    with tab2:
        st.markdown("## 🌍 Geographic Information Hallucination")
        st.markdown("**Risk:** GPT-2 will fabricate capitals, locations, and geographic features.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Test 3: Australian Capital")
            if st.button("Generate", key="geo1"):
                prompt = "The capital of Australia is"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">Canberra (NOT Sydney or Melbourne)</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
                
                st.markdown("**🚨 Check for:**")
                st.markdown('<div class="warning-box">• Sydney or Melbourne (common error)<br>• Invented city names<br>• Wrong population<br>• Fabricated facts</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Test 4: Mount Everest")
            if st.button("Generate", key="geo2"):
                prompt = "Mount Everest is located in"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">Nepal-Tibet border, height: 8,848.86 meters</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
                
                st.markdown("**🚨 Check for:**")
                st.markdown('<div class="warning-box">• Incorrect location<br>• Wrong height<br>• Invented mountains<br>• False climbing records</div>', unsafe_allow_html=True)
    
    # Tab 3: News Summarization
    with tab3:
        st.markdown("## 📰 News Summarization Hallucination")
        st.markdown("**Risk:** GPT-2 will add details, change facts, or invent quotes.")
        
        st.markdown("### Test 5: Battery Technology News")
        
        news_article = """A breakthrough study published in Nature revealed that scientists at MIT 
have developed a new battery technology that could extend electric vehicle range by 50%. 
The research team, led by Dr. Sarah Chen, tested the batteries over 1,000 charge cycles. 
The technology is expected to be commercially available by 2026."""
        
        st.markdown("**📄 Original Article:**")
        st.info(news_article)
        
        if st.button("Generate Summary", key="news1"):
            prompt = news_article + "\n\nTL;DR:"
            with st.spinner("Generating summary..."):
                output = generate_gpt2_text(model, tokenizer, prompt, max_length + 100, temperature)
            
            st.markdown("**✓ Ground Truth:**")
            st.markdown('<div class="truth-box">MIT scientists developed battery tech for 50% more EV range, tested 1,000 cycles, available 2026</div>', unsafe_allow_html=True)
            
            st.markdown("**❌ GPT-2 Output:**")
            st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
            
            st.markdown("**🚨 Check for:**")
            st.markdown('<div class="warning-box">• Changed percentages/numbers<br>• Invented names/institutions<br>• Fabricated quotes<br>• Added details not in original<br>• Changed dates</div>', unsafe_allow_html=True)
    
    # Tab 4: Question Answering
    with tab4:
        st.markdown("## ❓ Question Answering Hallucination")
        st.markdown("**Risk:** GPT-2 provides confident but incorrect answers.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Test 6: Continents")
            if st.button("Generate", key="qa1"):
                prompt = "Q: How many continents are there on Earth?\nA:"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">7 continents: Africa, Antarctica, Asia, Europe, North America, Australia, South America</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Test 7: Microsoft Founding")
            if st.button("Generate", key="qa2"):
                prompt = "Q: When was Microsoft founded?\nA:"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">April 4, 1975 by Bill Gates and Paul Allen in Albuquerque, New Mexico</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
    
    # Tab 5: Technical Explanation
    with tab5:
        st.markdown("## 🔬 Technical Explanation Hallucination")
        st.markdown("**Risk:** GPT-2 will add incorrect interpretations or fabricated context.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Test 8: Quantum Computing")
            if st.button("Generate", key="tech1"):
                prompt = "Quantum computing is"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">Computation using quantum phenomena like superposition and entanglement</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Test 9: Shakespeare's Hamlet")
            if st.button("Generate", key="tech2"):
                prompt = "Shakespeare's Hamlet was written in"
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, prompt, max_length, temperature)
                
                st.markdown("**📝 Prompt:**")
                st.code(prompt)
                
                st.markdown("**✓ Ground Truth:**")
                st.markdown('<div class="truth-box">Between 1599-1601, first published in 1603</div>', unsafe_allow_html=True)
                
                st.markdown("**❌ GPT-2 Output:**")
                st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
    
    # Tab 6: Custom Test
    with tab6:
        st.markdown("## 🎨 Custom Hallucination Test")
        st.markdown("**Try your own prompt to test GPT-2's hallucination tendencies!**")
        
        custom_prompt = st.text_area(
            "Enter your prompt:",
            placeholder="e.g., 'The first person on the moon was...'"
        )
        
        custom_truth = st.text_area(
            "Enter the ground truth (correct answer):",
            placeholder="e.g., 'Neil Armstrong on July 20, 1969'"
        )
        
        if st.button("Generate Custom Test", key="custom"):
            if custom_prompt and custom_truth:
                with st.spinner("Generating..."):
                    output = generate_gpt2_text(model, tokenizer, custom_prompt, max_length, temperature)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**✓ Ground Truth:**")
                    st.markdown(f'<div class="truth-box">{custom_truth}</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown("**❌ GPT-2 Output:**")
                    st.markdown(f'<div class="error-box">{output}</div>', unsafe_allow_html=True)
                
                st.markdown("**📊 Compare and identify hallucinations:**")
                st.markdown("Check if GPT-2's output contains factual errors, invented details, or contradictions with the ground truth.")
            else:
                st.warning("Please enter both a prompt and ground truth!")
    
    # Footer with key takeaways
    st.markdown("---")
    st.markdown("## 🎓 Key Takeaways")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### ❌ The Problem
        - Generates plausible but incorrect info
        - No fact-checking mechanism
        - Confidently wrong
        - Inconsistent outputs
        """)
    
    with col2:
        st.markdown("""
        ### 🔍 Why It Happens
        - Predicts word sequences, not facts
        - No knowledge representation
        - No uncertainty awareness
        - Pattern matching from training data
        """)
    
    with col3:
        st.markdown("""
        ### ⚠️ Real-World Impact
        - Unreliable for summarization
        - Dangerous for Q&A systems
        - Spreads misinformation
        - Unsuitable for critical applications
        """)
    
    st.markdown("---")
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ CRITICAL WARNING:</strong><br>
        GPT-2 is a powerful text generator but is <strong>NOT a reliable source of factual information</strong>. 
        Always verify AI-generated content, especially in medical, legal, financial, or news contexts.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
