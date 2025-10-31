"""
Setup Verification Script
Run this to check if your environment is properly configured.
"""

import sys

def check_python_version():
    """Check Python version"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"   ✗ Python {version.major}.{version.minor} (Need 3.8+)")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"   ✓ {package_name}")
        return True
    except ImportError:
        print(f"   ✗ {package_name} (NOT INSTALLED)")
        return False

def check_transformers_models():
    """Check if we can load transformers"""
    print("\n🤖 Checking Transformers library...")
    try:
        from transformers import T5Tokenizer
        print("   ✓ Transformers library loaded")
        # Try to create tokenizer (this will test sentencepiece)
        tokenizer = T5Tokenizer.from_pretrained('t5-base')
        print("   ✓ T5 tokenizer working (sentencepiece OK)")
        return True
    except ImportError as e:
        if 'sentencepiece' in str(e).lower():
            print(f"   ✗ SentencePiece library missing")
            print(f"   → Fix: pip install sentencepiece protobuf")
        else:
            print(f"   ✗ Import error: {str(e)}")
        return False
    except Exception as e:
        print(f"   ✗ Error loading model: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("  Beyond the Hype - Environment Verification")
    print("=" * 60)
    
    all_checks = []
    
    # Python version
    all_checks.append(check_python_version())
    
    # Core packages
    print("\n📦 Checking required packages...")
    packages = [
        ("transformers", "transformers"),
        ("torch", "torch"),
        ("sentencepiece", "sentencepiece"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("streamlit", "streamlit"),
        ("plotly", "plotly"),
        ("jupyter", "jupyter"),
    ]
    
    for package, import_name in packages:
        all_checks.append(check_package(package, import_name))
    
    # Transformers functionality
    all_checks.append(check_transformers_models())
    
    # Summary
    print("\n" + "=" * 60)
    if all(all_checks):
        print("✅ ALL CHECKS PASSED - You're ready to go!")
        print("\nNext steps:")
        print("  1. Run: jupyter notebook demo_notebook.ipynb")
        print("  2. Or run: streamlit run app.py")
        print("\n💡 Note: First run will download ~2-3GB of AI models")
    else:
        print("❌ SOME CHECKS FAILED")
        print("\nTo fix issues:")
        print("  1. Run: pip install -r requirements.txt")
        print("  2. If still failing, try: pip install sentencepiece protobuf")
        print("  3. Run this script again: python verify_setup.py")
        print("\n💡 If problems persist, see SETUP.md for troubleshooting")
    print("=" * 60)

if __name__ == "__main__":
    main()
