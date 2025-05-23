# 🚀 Enhanced BookNLP - Ready to Run!

This is an enhanced version of the original [BookNLP](https://github.com/dbamman/book-nlp) with significant improvements for modern Python environments and user experience.

## ✨ What's New in This Version

### 🔧 **Compatibility Fixes**
- ✅ **Python 3.11+ Support**: Updated for modern Python environments
- ✅ **SSL Certificate Issues Fixed**: Automatic handling of macOS SSL problems
- ✅ **PyTorch/Transformers Compatibility**: Resolved model loading issues with newer library versions
- ✅ **Automatic Model Downloads**: Models download seamlessly without manual intervention

### 📚 **Enhanced Documentation & Examples**
- 📖 **Complete Setup Guide**: Step-by-step instructions in `SETUP_AND_USAGE.md`
- 🎯 **Quick Test Scripts**: `quick_test.py` for small texts, `test_booknlp.py` for full novels
- 📊 **Character Analysis Tool**: `analyze_characters.py` for detailed character insights
- 🎨 **Rich Output Examples**: See what BookNLP can do with real examples

### 🛠️ **Developer Experience**
- 🐍 **Virtual Environment Setup**: Isolated, reproducible environment
- 📁 **Proper .gitignore**: Clean repository without cache files
- ⚡ **Performance Notes**: Timing information for different models and hardware
- 🔄 **Error Handling**: Better error messages and troubleshooting

## 🚀 Quick Start

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/booknlp.git
cd booknlp

# 2. Set up environment
python3.11 -m venv booknlp_env
source booknlp_env/bin/activate
pip install --upgrade pip

# 3. Install dependencies
pip install torch tensorflow spacy transformers
python -m spacy download en_core_web_sm
pip install -e .

# 4. Test with example
cd examples
python quick_test.py
```

## 📊 What BookNLP Accomplishes

BookNLP provides **state-of-the-art literary text analysis**:

1. **🎭 Character Recognition**: Identifies and clusters character mentions
2. **🔗 Coreference Resolution**: Links pronouns to characters ("she" → "Emma")  
3. **💬 Speaker Attribution**: Determines who said what in dialogue
4. **⚧️ Gender Inference**: Infers character gender from pronouns
5. **🎬 Action Extraction**: Character actions, possessions, descriptions
6. **🧠 Semantic Analysis**: Word categorization by meaning
7. **📖 Event Detection**: Identifies narrative events

## 📈 Performance Examples

**Processing Jane Austen's Emma (189K words):**
- **Small model on CPU**: ~3 minutes
- **Big model on GPU**: ~2-3 minutes  

**Processing small excerpt (233 words):**
- **Small model on CPU**: ~1.4 seconds

## 🎯 Example Output

After processing, you get rich character analysis like:

```
CHARACTER ID 108 (Emma)
   Total mentions: 3970
   Referential gender: she/her (83% confidence)
   Proper names: Emma (797), Mrs. Goddard (58)
   Pronouns: I (783), her (750), she (560)
   Actions performed: have, doing, liked, sat, sit
   Possessions: sister, mother, caresses
   Described as: youngest, aware, happy
```

## 🆚 Improvements Over Original

| Feature | Original BookNLP | Enhanced Version |
|---------|------------------|------------------|
| Python Support | 3.7 only | 3.11+ with compatibility |
| SSL Issues | Manual fixes needed | Auto-handled |
| Model Loading | Version conflicts | Auto-compatibility |
| Documentation | Basic README | Comprehensive guides |
| Examples | Minimal | Rich, tested examples |
| Character Analysis | Raw output | Beautiful visualization |
| Setup Process | Complex | One-command setup |

## 🙏 Credits

This enhanced version builds upon the excellent work of:
- **David Bamman** and team - Original BookNLP
- **Berkeley NLP Group** - Research and models

## 📄 License

MIT License (same as original BookNLP)

## 💡 Use Cases

Perfect for:
- 📚 **Digital Humanities Research**
- 🎓 **Literature Courses** 
- 📊 **Character Network Analysis**
- 🤖 **Automated Book Analysis**
- 🔬 **Narrative Structure Studies**

---

**Ready to analyze literature like never before!** 🚀 