"""
Markov Chain Character Prediction Simulator
Predicts whether the next character will be a vowel or consonant
based on transition probabilities learned from sample text.
"""

# Set USE_FILE to True to load text from a file, or False to use TEXT variable
USE_FILE = True
FILEPATH = "sample.txt"
TEXT = "The quick brown fox jumps over the lazy dog."


def classify_character(char):
    if not char.isalpha():
        return 'other'

    vowels = 'aeiouAEIOU'
    if char in vowels:
        return 'vowel'
    else:
        return 'consonant'


def load_text():
    if USE_FILE:
        try:
            with open(FILEPATH, 'r', encoding='utf-8') as f:
                text = f.read()
            print(f"Loaded text from '{FILEPATH}' ({len(text)} characters)\n")
            return text
        except FileNotFoundError:
            print(f"Error: File '{FILEPATH}' not found.")
            print("Falling back to TEXT variable.\n")
            return TEXT
    else:
        print(f"Using text from TEXT variable ({len(TEXT)} characters)\n")
        return TEXT


def build_markov_chain(text):
    # Initialize transition counters
    transitions = {
        'vowel': {'vowel': 0, 'consonant': 0},
        'consonant': {'vowel': 0, 'consonant': 0}
    }

    # Track previous character type
    prev_type = None

    # Iterate through text
    for char in text:
        curr_type = classify_character(char)

        # Skip non-alphabetic characters but don't break the chain
        if curr_type == 'other':
            continue

        # Record transition if we have a previous character
        if prev_type is not None:
            transitions[prev_type][curr_type] += 1

        prev_type = curr_type

    # Calculate probabilities
    chain = {
        'vowel': {'vowel': 0.0, 'consonant': 0.0},
        'consonant': {'vowel': 0.0, 'consonant': 0.0}
    }

    for state in ['vowel', 'consonant']:
        total = transitions[state]['vowel'] + transitions[state]['consonant']
        if total > 0:
            chain[state]['vowel'] = transitions[state]['vowel'] / total
            chain[state]['consonant'] = transitions[state]['consonant'] / total

    return chain, transitions


def print_markov_chain(chain, transitions):
    print("=" * 60)
    print("MARKOV CHAIN TRANSITION PROBABILITIES")
    print("=" * 60)
    print()
    print("                Next Character Type")
    print("              ┌─────────┬───────────┐")
    print("              │  Vowel  │ Consonant │")
    print("┌─────────────┼─────────┼───────────┤")
    print(f"│ Vowel       │ {chain['vowel']['vowel']:7.4f} │  {chain['vowel']['consonant']:7.4f}  │")
    print(f"│ Consonant   │ {chain['consonant']['vowel']:7.4f} │  {chain['consonant']['consonant']:7.4f}  │")
    print("└─────────────┴─────────┴───────────┘")
    print()

    # Print raw counts
    print("Raw Transition Counts:")
    total_v = transitions['vowel']['vowel'] + transitions['vowel']['consonant']
    total_c = transitions['consonant']['vowel'] + transitions['consonant']['consonant']
    print(f"  Vowel -> Vowel: {transitions['vowel']['vowel']} (out of {total_v})")
    print(f"  Vowel -> Consonant: {transitions['vowel']['consonant']} (out of {total_v})")
    print(f"  Consonant -> Vowel: {transitions['consonant']['vowel']} (out of {total_c})")
    print(f"  Consonant -> Consonant: {transitions['consonant']['consonant']} (out of {total_c})")
    print()


def test_accuracy(text, chain):
    """
    Test the accuracy of the Markov chain by predicting character types.

    Uses the chain to predict whether each next character will be a vowel
    or consonant based on the current character, then compares to actual.

    Args:
        text: Text to test on
        chain: Markov chain with transition probabilities

    Returns:
        float: Accuracy percentage
        int: Number of correct predictions
        int: Total predictions made
    """
    correct = 0
    total = 0
    prev_type = None

    for char in text:
        curr_type = classify_character(char)

        # Skip non-alphabetic characters
        if curr_type == 'other':
            continue

        # Make prediction if we have a previous character
        if prev_type is not None:
            # Predict the more likely transition
            if chain[prev_type]['vowel'] >= chain[prev_type]['consonant']:
                prediction = 'vowel'
            else:
                prediction = 'consonant'

            # Check if prediction is correct
            if prediction == curr_type:
                correct += 1
            total += 1

        prev_type = curr_type

    # Calculate accuracy
    accuracy = (correct / total * 100) if total > 0 else 0

    return accuracy, correct, total


def main():
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  MARKOV CHAIN CHARACTER PREDICTION SIMULATOR".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print()

    # Load text
    text = load_text()

    # Edge case
    alphabetic_chars = sum(1 for c in text if c.isalpha())
    if alphabetic_chars < 2:
        print("Error: Text must contain at least 2 alphabetic characters.")
        return

    # Build Markov chain
    chain, transitions = build_markov_chain(text)

    # Check if we have enough data
    total_transitions = sum(sum(transitions[state].values()) for state in transitions)
    if total_transitions == 0:
        print("Error: No character transitions found in text.")
        return

    # Print the chain
    print_markov_chain(chain, transitions)

    # Test accuracy
    print("=" * 60)
    print("ACCURACY TEST")
    print("=" * 60)
    print()
    accuracy, correct, total = test_accuracy(text, chain)

    print(f"Predictions: {correct} correct out of {total} total")
    print(f"Accuracy: {accuracy:.2f}%")
    print()

    # Summary statistics
    vowel_count = sum(1 for c in text if classify_character(c) == 'vowel')
    consonant_count = sum(1 for c in text if classify_character(c) == 'consonant')

    print("=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(f"Total characters analyzed: {len(text)}")
    print(f"Alphabetic characters: {alphabetic_chars}")
    print(f"  Vowels: {vowel_count} ({vowel_count/alphabetic_chars*100:.1f}%)")
    print(f"  Consonants: {consonant_count} ({consonant_count/alphabetic_chars*100:.1f}%)")
    print(f"Total transitions tracked: {total_transitions}")
    print()


if __name__ == "__main__":
    main()
