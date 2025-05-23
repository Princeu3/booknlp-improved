# BookNLP Setup and Usage Guide

This guide shows you how to get BookNLP running on your system and provides examples of its powerful literary analysis capabilities.

## Quick Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment with Python 3.11+
python3.11 -m venv booknlp_env
source booknlp_env/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### 2. Install Dependencies

```bash
# Install all required packages
pip install torch tensorflow spacy transformers

# Download spacy English model
python -m spacy download en_core_web_sm

# Install BookNLP in development mode
pip install -e .
```

### 3. Test Installation

```bash
cd examples
python -c "from booknlp.booknlp import BookNLP; print('BookNLP import successful!')"
```

## Basic Usage

### Simple Example

```python
from booknlp.booknlp import BookNLP

# Initialize BookNLP with small model (faster)
model_params = {
    "pipeline": "entity,quote,supersense,event,coref", 
    "model": "small"  # or "big" for better accuracy
}

booknlp = BookNLP("en", model_params)

# Process a text file
input_file = "your_book.txt"
output_directory = "output/"
book_id = "my_book"

booknlp.process(input_file, output_directory, book_id)
```

### Processing the Example

```bash
cd examples
python test_booknlp.py
```

## Output Files

BookNLP generates several output files with rich linguistic annotations:

### 1. `.entities` - Named Entity Recognition & Coreference
```
COREF	start_token	end_token	prop	cat	text
108	4	5	PROP	PER	Emma Woodhouse
108	51	51	PRON	PER	her
108	53	53	PRON	PER	She
```

### 2. `.quotes` - Quotation & Speaker Attribution  
```
quote_start	quote_end	mention_start	mention_end	mention_phrase	char_id	quote
1272	1295	1266	1266	he	431	" Poor Miss Taylor!--I wish she were here again..."
```

### 3. `.tokens` - Part-of-Speech & Dependency Parsing
```
paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event
0	0	0	0	VOLUME	volume	0	6	NOUN	NN	compound	1	O
```

### 4. `.supersense` - Semantic Categories
```
start_token	end_token	supersense_category	text
4	5	noun.person	Emma Woodhouse
17	17	noun.artifact	home
20	20	noun.attribute	disposition
```

### 5. `.book` - Character Analysis (JSON)
Rich character profiles including:
- Proper names, common names, pronouns
- Actions performed and received  
- Possessions and descriptive modifiers
- Referential gender inference
- Relationship networks

### 6. `.book.html` - Interactive Visualization
Beautiful HTML visualization with:
- Annotated text with entity highlighting
- Character lists with mention counts
- Major entity categories (places, organizations, etc.)

## Character Analysis

Use the provided character analysis script:

```bash
python analyze_characters.py output/my_book.book
```

This displays detailed character information including:
- Mention counts and referential gender
- Names and pronouns used
- Actions, possessions, and descriptors
- Character relationships

## Pipeline Components

You can customize which components to run:

```python
model_params = {
    "pipeline": "entity,quote,supersense,event,coref",  # Full pipeline
    # "pipeline": "entity,quote",  # Just entities and quotes
    # "pipeline": "entity,coref",  # Just entities and coreference
    "model": "small"
}
```

Available components:
- **entity**: Named entity recognition
- **quote**: Quotation detection  
- **supersense**: Semantic categorization
- **event**: Event detection
- **coref**: Coreference resolution

## Model Options

- **small**: Faster processing, good accuracy (recommended for laptops)
- **big**: Better accuracy, requires more resources (recommended for servers/GPUs)

## Performance Notes

Processing times for Jane Austen's Emma (189K words):
- **Small model on CPU**: ~3 minutes
- **Big model on GPU**: ~2-3 minutes  
- **Big model on CPU**: ~15-20 minutes

## Troubleshooting

### SSL Certificate Issues
If you encounter SSL errors during model download, the code automatically handles this by disabling SSL verification for model downloads.

### Model Compatibility Issues  
The code automatically handles PyTorch/Transformers version compatibility by removing problematic keys from older saved models.

### Memory Issues
If you run out of memory:
1. Use the "small" model instead of "big"
2. Process shorter texts
3. Reduce batch size by modifying the code

## What BookNLP Accomplishes

BookNLP provides state-of-the-art literary text analysis:

1. **Character Recognition**: Identifies and clusters character mentions across an entire book
2. **Coreference Resolution**: Links pronouns to their referents ("she" → "Emma")  
3. **Speaker Attribution**: Determines who said what in dialogue
4. **Gender Inference**: Infers character gender from pronoun usage
5. **Relationship Extraction**: Identifies character actions, possessions, and descriptions
6. **Semantic Analysis**: Categorizes words by meaning (places, emotions, actions, etc.)
7. **Event Detection**: Identifies significant events in the narrative

This makes BookNLP invaluable for:
- Literary analysis and digital humanities research
- Character network analysis
- Narrative structure studies  
- Automated book summarization
- Educational tools for literature courses

## Citation

If you use BookNLP in your research, please cite:
```
Bamman, David, Sejal Popat and Sheng Shen, "An Annotated Dataset of Literary Entities," NAACL 2019.
```

## Support

For issues and questions:
- Check the original repository: https://github.com/dbamman/book-nlp
- Review the academic papers linked in the main README
- Open issues for specific bugs or feature requests 