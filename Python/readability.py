from cs50 import get_string
import string

def count_letters(text):
    """Count alphabetic characters in text"""
    return sum(1 for char in text if char.isalpha())

def count_words(text):
    """Count words in text (separated by spaces)"""
    return len(text.split())

def count_sentences(text):
    """Count sentences in text (ending with . ! ?)"""
    return sum(1 for char in text if char in '.!?')

def calculate_grade(text):
    """Calculate Coleman-Liau readability grade"""
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    
    if words == 0:
        return 0
    
    # Coleman-Liau formula
    L = (letters / words) * 100  # Average letters per 100 words
    S = (sentences / words) * 100  # Average sentences per 100 words
    
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

def analyze_text(text):
    """Provide detailed text analysis"""
    analysis = {
        'letters': count_letters(text),
        'words': count_words(text),
        'sentences': count_sentences(text),
        'characters': len(text),
        'paragraphs': len([p for p in text.split('\n\n') if p.strip()])
    }
    return analysis

def main():
    """Text readability analyzer"""
    
    text = get_string("Text: ")
    
    # Calculate grade level
    grade = calculate_grade(text)
    
    # Display result
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")
    
    # Detailed analysis
    print("\nDetailed Analysis:")
    analysis = analyze_text(text)
    
    for key, value in analysis.items():
        print(f"{key.capitalize()}: {value}")
    
    # Calculate reading time (average 200 words per minute)
    reading_time = analysis['words'] / 200
    print(f"Estimated reading time: {reading_time:.1f} minutes")

if __name__ == "__main__":
    main()
