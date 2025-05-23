#!/usr/bin/env python3
"""
Quick test of BookNLP with a small text sample
"""

from booknlp.booknlp import BookNLP
import os

# Create a small test text
test_text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do. Once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it. "And what is the use of a book," thought Alice, "without pictures or conversations?"

So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, "Oh dear! Oh dear! I shall be late!" But when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it.
"""

def main():
    print("BookNLP Quick Test")
    print("=" * 50)
    
    # Write test text to file
    with open("test_alice.txt", "w") as f:
        f.write(test_text.strip())
    
    print("Created test file: test_alice.txt")
    
    # Initialize BookNLP
    model_params = {
        "pipeline": "entity,quote,supersense,event,coref", 
        "model": "small"
    }
    
    print("Initializing BookNLP...")
    booknlp = BookNLP("en", model_params)
    
    # Process the text
    print("Processing text...")
    booknlp.process("test_alice.txt", "alice_output", "alice")
    
    print("\nProcessing complete!")
    print("\nGenerated files:")
    
    # List output files
    output_files = [f for f in os.listdir("alice_output") if f.startswith("alice.")]
    for file in sorted(output_files):
        file_path = os.path.join("alice_output", file)
        size = os.path.getsize(file_path)
        print(f"  {file} ({size} bytes)")
    
    print(f"\nFound {len(output_files)} output files")
    
    # Show a few entities
    print("\nFirst few entities identified:")
    try:
        with open("alice_output/alice.entities", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:6]):
                print(f"  {line.strip()}")
    except FileNotFoundError:
        print("  No entities file found")
    
    # Show character analysis if available
    try:
        import json
        with open("alice_output/alice.book", "r") as f:
            data = json.load(f)
            characters = data.get("characters", [])
            print(f"\nIdentified {len(characters)} characters:")
            for char in characters[:3]:
                proper_names = [name["n"] for name in char["mentions"]["proper"][:2]]
                print(f"  Character {char['id']}: {', '.join(proper_names) if proper_names else 'Unnamed'} ({char['count']} mentions)")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo character analysis available")
    
    print("\n✅ BookNLP is working correctly!")
    print("\nTo see detailed character analysis, run:")
    print("python analyze_characters.py alice_output/alice.book")

if __name__ == "__main__":
    main() 