#!/usr/bin/env python3
"""
Simple script to analyze character information extracted by BookNLP
"""

import json
import sys

def analyze_characters(book_file):
    """Analyze character data from BookNLP output"""
    
    with open(book_file, 'r') as f:
        data = json.load(f)
    
    print("=" * 60)
    print("BOOKNLP CHARACTER ANALYSIS")
    print("=" * 60)
    
    characters = data.get('characters', [])
    
    print(f"\nFound {len(characters)} major characters mentioned more than once:\n")
    
    for i, char in enumerate(characters[:10]):  # Show top 10 characters
        print(f"{i+1}. CHARACTER ID {char['id']}")
        print(f"   Total mentions: {char['count']}")
        
        # Gender
        gender = char.get('g', 'Unknown')
        if gender:
            if isinstance(gender, list) and len(gender) > 0:
                gender = gender[0] if gender[0] else 'Unknown'
        print(f"   Referential gender: {gender}")
        
        # Proper names
        proper_names = char['mentions']['proper']
        if proper_names:
            names = [f"{name['n']} ({name['c']})" for name in proper_names[:3]]
            print(f"   Proper names: {', '.join(names)}")
        
        # Common names
        common_names = char['mentions']['common']
        if common_names:
            names = [f"{name['n']} ({name['c']})" for name in common_names[:3]]
            print(f"   Common names: {', '.join(names)}")
        
        # Pronouns
        pronouns = char['mentions']['pronoun']
        if pronouns:
            prns = [f"{name['n']} ({name['c']})" for name in pronouns[:3]]
            print(f"   Pronouns: {', '.join(prns)}")
        
        # Actions as agent
        if char['agent']:
            actions = [action['w'] for action in char['agent'][:5]]
            print(f"   Actions performed: {', '.join(actions)}")
        
        # Actions as patient
        if char['patient']:
            actions = [action['w'] for action in char['patient'][:3]]
            print(f"   Actions received: {', '.join(actions)}")
        
        # Possessions
        if char['poss']:
            possessions = [item['w'] for item in char['poss'][:3]]
            print(f"   Possessions: {', '.join(possessions)}")
        
        # Modifiers
        if char['mod']:
            modifiers = [mod['w'] for mod in char['mod'][:3]]
            print(f"   Described as: {', '.join(modifiers)}")
        
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_characters.py <book_file.book>")
        print("Example: python analyze_characters.py test_output/emma_test.book")
        sys.exit(1)
    
    book_file = sys.argv[1]
    analyze_characters(book_file) 