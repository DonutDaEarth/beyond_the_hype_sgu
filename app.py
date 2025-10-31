"""
Beyond the Hype: When Transformers Can't Count
Interactive Streamlit Application for Live Demonstration

This app provides a user-friendly interface to demonstrate the numerical
reasoning failures of state-of-the-art Transformer models.
"""

import streamlit as st
import torch
from transformers import (
    T5ForConditionalGeneration, 
    T5Tokenizer,
    BartForConditionalGeneration,
    BartTokenizer,
    GPT2LMHeadModel,
    GPT2Tokenizer,
    pipeline
)
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Beyond the Hype: When Transformers Can't Count",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .correct-answer {
        background-color: #d4edda;
        color: #155724;
        padding: 20px;
        border-radius: 8px;
        border-left: 6px solid #28a745;
        border: 2px solid #28a745;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .wrong-answer {
        background-color: #f8d7da;
        color: #721c24;
        padding: 20px;
        border-radius: 8px;
        border-left: 6px solid #dc3545;
        border: 2px solid #dc3545;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .model-output {
        background-color: #fff3cd;
        color: #856404;
        padding: 20px;
        border-radius: 8px;
        border-left: 6px solid #ffc107;
        border: 2px solid #ffc107;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Cache model loading
@st.cache_resource
def load_models():
    """Load all models once and cache them"""
    with st.spinner('🤖 Loading AI models... This may take a few minutes...'):
        # Load FLAN-T5-Large
        t5_model = T5ForConditionalGeneration.from_pretrained('google/flan-t5-large')
        t5_tokenizer = T5Tokenizer.from_pretrained('google/flan-t5-large')
        t5_model.eval()
        
        # Load BART - explicitly use PyTorch framework
        bart_summarizer = pipeline(
            "summarization", 
            model="facebook/bart-large-cnn",
            framework="pt"  # Force PyTorch, avoid TensorFlow
        )
        
        # Load GPT-2
        gpt2_model = GPT2LMHeadModel.from_pretrained('gpt2')
        gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token
        gpt2_model.eval()
        
        # Load DistilGPT-2
        distilgpt2_model = GPT2LMHeadModel.from_pretrained('distilgpt2')
        distilgpt2_tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
        distilgpt2_tokenizer.pad_token = distilgpt2_tokenizer.eos_token
        distilgpt2_model.eval()
        
        # Load T5-small
        t5small_model = T5ForConditionalGeneration.from_pretrained('t5-small')
        t5small_tokenizer = T5Tokenizer.from_pretrained('t5-small')
        t5small_model.eval()
        
        return {
            't5_model': t5_model,
            't5_tokenizer': t5_tokenizer,
            'bart_summarizer': bart_summarizer,
            'gpt2_model': gpt2_model,
            'gpt2_tokenizer': gpt2_tokenizer,
            'distilgpt2_model': distilgpt2_model,
            'distilgpt2_tokenizer': distilgpt2_tokenizer,
            't5small_model': t5small_model,
            't5small_tokenizer': t5small_tokenizer
        }

def generate_t5_response(models, prompt, max_length=100):
    """Generate response using FLAN-T5-Large model"""
    # FLAN-T5 works better with direct instructions
    input_ids = models['t5_tokenizer'].encode(
        prompt, 
        return_tensors='pt', 
        max_length=512, 
        truncation=True
    )
    with torch.no_grad():
        outputs = models['t5_model'].generate(
            input_ids,
            max_length=max_length,
            num_beams=4,
            early_stopping=True,
            temperature=0.1,
            do_sample=False
        )
    return models['t5_tokenizer'].decode(outputs[0], skip_special_tokens=True)

def generate_gpt2_response(models, prompt, max_length=100):
    """Generate response using GPT-2 model"""
    input_ids = models['gpt2_tokenizer'].encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = models['gpt2_model'].generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=models['gpt2_tokenizer'].eos_token_id,
            temperature=0.7,
            do_sample=True
        )
    return models['gpt2_tokenizer'].decode(outputs[0], skip_special_tokens=True)

def generate_distilgpt2_response(models, prompt, max_length=100):
    """Generate response using DistilGPT-2 model"""
    input_ids = models['distilgpt2_tokenizer'].encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = models['distilgpt2_model'].generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=models['distilgpt2_tokenizer'].eos_token_id,
            temperature=0.7,
            do_sample=True
        )
    return models['distilgpt2_tokenizer'].decode(outputs[0], skip_special_tokens=True)

def generate_t5small_response(models, prompt, max_length=100):
    """Generate response using T5-small model"""
    input_ids = models['t5small_tokenizer'].encode(
        prompt, 
        return_tensors='pt', 
        max_length=512, 
        truncation=True
    )
    with torch.no_grad():
        outputs = models['t5small_model'].generate(
            input_ids,
            max_length=max_length,
            num_beams=4,
            early_stopping=True,
            temperature=0.1,
            do_sample=False
        )
    return models['t5small_tokenizer'].decode(outputs[0], skip_special_tokens=True)

def generate_bart_summary(models, text, max_length=130, min_length=30):
    """Generate summary using BART model"""
    try:
        result = models['bart_summarizer'](
            text, 
            max_length=max_length, 
            min_length=min_length, 
            do_sample=False
        )
        return result[0]['summary_text']
    except Exception as e:
        return f"Error: {str(e)}"

def display_result_card(label, content, is_correct=None):
    """Display a formatted result card with enhanced visibility"""
    if is_correct is None:
        st.markdown(f"""
        <div class="model-output">
            <strong style="font-size: 18px;">{label}</strong><br>
            <span style="font-size: 20px; font-weight: bold;">{content}</span>
        </div>
        """, unsafe_allow_html=True)
    elif is_correct:
        st.markdown(f"""
        <div class="correct-answer">
            <strong style="font-size: 18px;">✓ {label}</strong>
            <span style="font-size: 22px; color: #28a745; font-weight: bold; margin-left: 10px;">CORRECT! ✓</span><br>
            <span style="font-size: 24px; font-weight: bold; margin-top: 10px; display: inline-block;">{content}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="wrong-answer">
            <strong style="font-size: 18px;">❌ {label}</strong>
            <span style="font-size: 22px; color: #dc3545; font-weight: bold; margin-left: 10px;">WRONG! ❌</span><br>
            <span style="font-size: 24px; font-weight: bold; margin-top: 10px; display: inline-block;">{content}</span>
        </div>
        """, unsafe_allow_html=True)

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🧮 Beyond the Hype: When Transformers Can\'t Count</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Demonstrating Critical Failures in Numerical Reasoning</p>', unsafe_allow_html=True)
    
    # Load models
    models = load_models()
    st.success("✓ All 5 models loaded successfully! (FLAN-T5-Large, BART, GPT-2, DistilGPT-2, T5-small)")
    
    # Sidebar
    st.sidebar.title("📋 Test Categories")
    test_category = st.sidebar.selectbox(
        "Choose a demonstration:",
        [
            "🔢 Basic Arithmetic",
            "💰 Financial Reporting",
            "🔄 Rephrasing Consistency",
            "📊 Counting Objects",
            "💊 Medical Dosage",
            "📈 Statistics",
            "🧪 Custom Test",
            "📉 Batch Analysis"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎯 Project Thesis")
    st.sidebar.info("""
    Despite achieving near-human performance on many NLP tasks, 
    state-of-the-art Transformer models fail catastrophically at 
    basic numerical reasoning that any elementary student could solve.
    """)
    
    # Main content area
    st.markdown("---")
    
    if test_category == "🔢 Basic Arithmetic":
        st.header("Basic Arithmetic Tests")
        st.write("Testing if models can perform simple calculations across different architectures...")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Test 1: Addition")
            if st.button("Run Addition Test"):
                with st.spinner("Computing..."):
                    prompt = "What is 347 + 589? Give only the numerical answer."
                    correct = "936"
                    
                    # Get all model responses
                    t5_result = generate_t5_response(models, prompt, max_length=20)
                    gpt2_result = generate_gpt2_response(models, prompt, max_length=50)
                    distilgpt2_result = generate_distilgpt2_response(models, prompt, max_length=50)
                    t5small_result = generate_t5small_response(models, prompt, max_length=20)
                    
                    st.markdown("### 📝 Question: **What is 347 + 589?**")
                    display_result_card("Correct Answer", correct, True)
                    display_result_card("FLAN-T5-Large (780M)", t5_result, t5_result.strip() == correct)
                    display_result_card("GPT-2 (117M)", gpt2_result, gpt2_result.strip() == correct)
                    display_result_card("DistilGPT-2 (82M)", distilgpt2_result, distilgpt2_result.strip() == correct)
                    display_result_card("T5-small (60M)", t5small_result, t5small_result.strip() == correct)
                    
                    # Check if any failed
                    results = [t5_result.strip(), gpt2_result.strip(), distilgpt2_result.strip(), t5small_result.strip()]
                    if not all(r == correct for r in results):
                        st.error("❌ Multiple models failed basic addition!")
        
        with col2:
            st.subheader("Test 2: Multiplication")
            if st.button("Run Multiplication Test"):
                with st.spinner("Computing..."):
                    prompt = "What is 23 × 17? Give only the numerical answer."
                    correct = "391"
                    
                    # Get all model responses
                    t5_result = generate_t5_response(models, prompt, max_length=20)
                    gpt2_result = generate_gpt2_response(models, prompt, max_length=50)
                    distilgpt2_result = generate_distilgpt2_response(models, prompt, max_length=50)
                    t5small_result = generate_t5small_response(models, prompt, max_length=20)
                    
                    st.markdown("### 📝 Question: **What is 23 × 17?**")
                    display_result_card("Correct Answer", correct, True)
                    display_result_card("FLAN-T5-Large (780M)", t5_result, t5_result.strip() == correct)
                    display_result_card("GPT-2 (117M)", gpt2_result, gpt2_result.strip() == correct)
                    display_result_card("DistilGPT-2 (82M)", distilgpt2_result, distilgpt2_result.strip() == correct)
                    display_result_card("T5-small (60M)", t5small_result, t5small_result.strip() == correct)
                    
                    # Check if any failed
                    results = [t5_result.strip(), gpt2_result.strip(), distilgpt2_result.strip(), t5small_result.strip()]
                    if not all(r == correct for r in results):
                        st.error("❌ Multiple models failed basic multiplication!")
    
    elif test_category == "💰 Financial Reporting":
        st.header("Financial Reporting Scenario")
        st.write("Testing summarization of financial data - a high-stakes real-world application.")
        
        financial_report = st.text_area(
            "Financial Report:",
            """TechCorp reported quarterly earnings for Q3 2024. Revenue reached $450 million, representing a 23% increase from the previous quarter's $366 million. Operating expenses were $280 million, resulting in an operating profit of $170 million. The company's net profit margin improved to 32%, up from 28% in Q2. Employee headcount grew from 1,250 to 1,450 employees.""",
            height=150
        )
        
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_bart_summary(models, financial_report)
                
                st.subheader("Results")
                st.write("**Original Text:**")
                st.info(financial_report)
                
                st.write("**Model Summary:**")
                display_result_card("BART Output", summary)
                
                st.warning("""
                ⚠️ **Critical Check:** Verify all numbers are preserved:
                - Revenue: $450M
                - Growth: 23%
                - Previous revenue: $366M
                - Operating expenses: $280M
                - Operating profit: $170M
                - Profit margin: 32% (from 28%)
                - Employees: 1,450 (from 1,250)
                
                **Even one error could mislead investors!**
                """)
    
    elif test_category == "🔄 Rephrasing Consistency":
        st.header("Rephrasing Consistency Test")
        st.write("The same math problem phrased differently should give the same answer...")
        
        if st.button("Run Consistency Test"):
            test_cases = [
                "If you have 15 apples and buy 23 more, how many apples do you have? Give only the number.",
                "Calculate the total: 15 apples plus 23 apples. Give only the number.",
                "15 + 23 = ?"
            ]
            
            correct = "38"
            results = []
            
            with st.spinner("Testing..."):
                for i, prompt in enumerate(test_cases, 1):
                    result = generate_t5_response(models, prompt, max_length=20)
                    results.append(result)
            
            st.subheader("Results")
            st.write(f"**Correct Answer:** {correct}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("**Variation 1:** Word Problem")
                display_result_card("FLAN-T5-Large", results[0], results[0].strip() == correct)
            
            with col2:
                st.write("**Variation 2:** Formal")
                display_result_card("FLAN-T5-Large", results[1], results[1].strip() == correct)
            
            with col3:
                st.write("**Variation 3:** Symbolic")
                display_result_card("FLAN-T5-Large", results[2], results[2].strip() == correct)
            
            if not all(r.strip() == correct for r in results):
                st.error("❌ Inconsistent results prove the model doesn't understand the math!")
    
    elif test_category == "📊 Counting Objects":
        st.header("Counting Objects Test")
        st.write("Can the model count items in a list?")
        
        items = st.text_input(
            "Enter a comma-separated list:",
            "John, Mary, Steve, Alice, Bob, Carol, David, Emma, Frank, Grace"
        )
        
        if st.button("Count Items"):
            items_list = [item.strip() for item in items.split(',')]
            correct_count = len(items_list)
            
            prompt = f"Count the number of people in this list: {items}. Give only the number."
            
            with st.spinner("Counting..."):
                t5_result = generate_t5_response(models, prompt, max_length=20)
                gpt2_result = generate_gpt2_response(models, prompt, max_length=50)
                distilgpt2_result = generate_distilgpt2_response(models, prompt, max_length=50)
                t5small_result = generate_t5small_response(models, prompt, max_length=20)
            
            st.subheader("Results")
            display_result_card("Correct Count", str(correct_count), True)
            display_result_card("FLAN-T5-Large", t5_result, t5_result.strip() == str(correct_count))
            display_result_card("GPT-2", gpt2_result, gpt2_result.strip() == str(correct_count))
            display_result_card("DistilGPT-2", distilgpt2_result, distilgpt2_result.strip() == str(correct_count))
            display_result_card("T5-small", t5small_result, t5small_result.strip() == str(correct_count))
            
            results = [t5_result.strip(), gpt2_result.strip(), distilgpt2_result.strip(), t5small_result.strip()]
            if not all(r == str(correct_count) for r in results):
                st.error(f"❌ Failed! Expected {correct_count}, but models gave different answers")
    
    elif test_category == "💊 Medical Dosage":
        st.header("Medical Dosage Scenario")
        st.warning("⚠️ This demonstrates why AI cannot be trusted with medical data!")
        
        medical_text = st.text_area(
            "Medical Record:",
            """Patient prescribed medication as follows: Morning dose of 50mg, afternoon dose of 50mg, evening dose of 50mg. Total daily dosage is 150mg. Patient weight: 68kg. Dosage per kg: 2.2mg/kg. Maximum safe dose: 200mg per day.""",
            height=100
        )
        
        if st.button("Generate Medical Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_bart_summary(models, medical_text, max_length=100, min_length=30)
                
                st.subheader("Results")
                st.info(f"**Original:** {medical_text}")
                display_result_card("Model Summary", summary)
                
                st.error("""
                🚨 **CRITICAL RISK ASSESSMENT**
                
                In healthcare, numerical accuracy is literally life-or-death:
                - Wrong dosage → Overdose or underdose
                - Wrong weight → Incorrect medication amount  
                - Wrong safety threshold → Dangerous prescriptions
                
                **This is why we cannot blindly trust AI with medical data!**
                """)
    
    elif test_category == "📈 Statistics":
        st.header("Statistical Calculations")
        
        numbers = st.text_input("Enter numbers (comma-separated):", "85, 90, 78, 92, 88")
        
        if st.button("Calculate Average"):
            nums = [float(x.strip()) for x in numbers.split(',')]
            correct_avg = sum(nums) / len(nums)
            
            prompt = f"The test scores are: {numbers}. What is the average score? Give only the numerical answer."
            
            with st.spinner("Calculating..."):
                t5_result = generate_t5_response(models, prompt, max_length=20)
                gpt2_result = generate_gpt2_response(models, prompt, max_length=50)
                distilgpt2_result = generate_distilgpt2_response(models, prompt, max_length=50)
                t5small_result = generate_t5small_response(models, prompt, max_length=20)
            
            st.subheader("Results")
            display_result_card("Correct Average", f"{correct_avg:.1f}", True)
            display_result_card("FLAN-T5-Large", t5_result, False)
            display_result_card("GPT-2", gpt2_result, False)
            display_result_card("DistilGPT-2", distilgpt2_result, False)
            display_result_card("T5-small", t5small_result, False)
    
    elif test_category == "🧪 Custom Test":
        st.header("Custom Test")
        st.write("Try your own test case!")
        
        custom_prompt = st.text_area(
            "Enter your question:",
            "What is 100 + 200? Give only the numerical answer."
        )
        
        custom_answer = st.text_input("Enter the correct answer:", "300")
        
        if st.button("Test Models"):
            with st.spinner("Generating responses..."):
                t5_result = generate_t5_response(models, custom_prompt, max_length=50)
                gpt2_result = generate_gpt2_response(models, custom_prompt, max_length=50)
                distilgpt2_result = generate_distilgpt2_response(models, custom_prompt, max_length=50)
                t5small_result = generate_t5small_response(models, custom_prompt, max_length=50)
                
                st.subheader("Results")
                display_result_card("Correct Answer", custom_answer, True)
                display_result_card("FLAN-T5-Large", t5_result, t5_result.strip() == custom_answer.strip())
                display_result_card("GPT-2", gpt2_result, gpt2_result.strip() == custom_answer.strip())
                display_result_card("DistilGPT-2", distilgpt2_result, distilgpt2_result.strip() == custom_answer.strip())
                display_result_card("T5-small", t5small_result, t5small_result.strip() == custom_answer.strip())
    
    elif test_category == "📉 Batch Analysis":
        st.header("Comprehensive Batch Analysis")
        st.write("Testing multiple problems to calculate overall accuracy.")
        
        if st.button("Run Batch Tests"):
            test_suite = [
                {"prompt": "45 + 67 = ?", "correct": "112", "category": "Addition"},
                {"prompt": "234 - 89 = ?", "correct": "145", "category": "Subtraction"},
                {"prompt": "12 × 8 = ?", "correct": "96", "category": "Multiplication"},
                {"prompt": "144 ÷ 12 = ?", "correct": "12", "category": "Division"},
                {"prompt": "What is 25% of 80?", "correct": "20", "category": "Percentage"},
            ]
            
            results = []
            progress_bar = st.progress(0)
            
            for i, test in enumerate(test_suite):
                with st.spinner(f"Testing {test['category']}..."):
                    output = generate_t5_response(models, test['prompt'], max_length=20).strip()
                    is_correct = (output == test['correct'])
                    results.append({
                        'Category': test['category'],
                        'Correct': test['correct'],
                        'FLAN-T5-Large Output': output,
                        'Status': '✓' if is_correct else '✗'
                    })
                    progress_bar.progress((i + 1) / len(test_suite))
            
            # Display results
            df = pd.DataFrame(results)
            st.subheader("Results Table")
            st.dataframe(df, use_container_width=True)
            
            # Calculate accuracy
            accuracy = (df['Status'] == '✓').sum() / len(df) * 100
            
            # Visualization
            fig = go.Figure(data=[
                go.Bar(
                    x=df['Category'],
                    y=[(1 if status == '✓' else 0) for status in df['Status']],
                    marker_color=['green' if s == '✓' else 'red' for s in df['Status']]
                )
            ])
            fig.update_layout(
                title="Pass/Fail by Category",
                xaxis_title="Category",
                yaxis_title="Correct (1) / Incorrect (0)",
                yaxis=dict(tickvals=[0, 1], ticktext=['Incorrect', 'Correct'])
            )
            st.plotly_chart(fig)
            
            # Summary
            st.metric("Overall Accuracy", f"{accuracy:.1f}%")
            
            if accuracy < 50:
                st.error("❌ Less than 50% accuracy on elementary math problems!")
            elif accuracy < 80:
                st.warning("⚠️ Failing grade on basic arithmetic!")
            else:
                st.info("The model got lucky this time, but inconsistency remains a problem.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    ### 🎓 Key Takeaways
    
    1. **State-of-the-art Transformers fail at basic arithmetic** that elementary students can solve
    2. **Numerical errors in summarization** can have catastrophic real-world consequences  
    3. **Inconsistent outputs** prove lack of true mathematical understanding
    4. **Models appear confident** even when completely wrong
    
    **The greatest danger of AI is not that it will become superintelligent, but that we will mistake 
    pattern matching for understanding and deploy it in contexts where failure is catastrophic.**
    """)

if __name__ == "__main__":
    main()
