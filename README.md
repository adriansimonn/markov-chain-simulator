## Markov Chain Character Prediction Simulator

A simple script that demonstrates Markov chain probability modeling by predicting whether the next character in a text sequence will be a vowel or consonant based on the current character type. Not a serious project, but a basic introduction to markov chains.

## Mathematical Explanation

### What is a Markov Chain?

A Markov chain is a mathematical model that describes a sequence of events where the probability of each event depends only on the state of the previous event, not on the entire history. This is known as the "memoryless" or Markov property.

### How This Model Works

This simulator simplifies characters into two types:
- **Vowels**: a, e, i, o, u (case-insensitive)
- **Consonants**: all other alphabetic characters

The Markov chain tracks four possible transitions:
1. Vowel → Vowel (V→V)
2. Vowel → Consonant (V→C)
3. Consonant → Vowel (C→V)
4. Consonant → Consonant (C→C)

### Calculating Transition Probabilities

For each transition type, the probability is calculated as:

```
P(next = type | current = state) = count(state → type) / total_transitions_from_state
```

For example:
```
P(Vowel | Vowel) = (Vowel→Vowel transitions) / (all transitions from Vowel)
```

The sum of probabilities for each current state must equal 1.0:
```
P(V|V) + P(C|V) = 1.0
P(V|C) + P(C|C) = 1.0
```

### Prediction Model

Once the Markov chain is built, the model predicts the next character type by choosing the transition with the higher probability from the current state. For example, if we're at a vowel and P(V|V) = 0.35 and P(C|V) = 0.65, the model predicts the next character will be a consonant.

## Usage Instructions

### Basic Usage

1. **Run with the included sample text:**
   ```bash
   python script.py
   ```

2. **Use your own text file:**
   - Place your `.txt` file in the same directory as `script.py`
   - Open `script.py` and modify the `FILEPATH` variable:
     ```python
     FILEPATH = "your_file.txt"
     ```
   - Ensure `USE_FILE = True`
   - Run the script:
     ```bash
     python script.py
     ```

3. **Use text directly in the code:**
   - Open `script.py`
   - Set `USE_FILE = False`
   - Modify the `TEXT` variable with your desired text:
     ```python
     TEXT = "Your custom text goes here."
     ```
   - Run the script:
     ```bash
     python script.py
     ```

### Configuration Variables

At the top of `script.py`, you'll find these configuration options:

```python
USE_FILE = True              # True: load from file, False: use TEXT variable
FILEPATH = "sample.txt"      # Path to your text file
TEXT = "Default text..."     # Direct text input (used when USE_FILE = False)
```

## Example Output

```
╔═════════════════════════════════════════════════════════╗
║                                                         ║
║    MARKOV CHAIN CHARACTER PREDICTION SIMULATOR          ║
║                                                         ║
╚═════════════════════════════════════════════════════════╝

Loaded text from 'sample.txt' (1337 characters)

============================================================
MARKOV CHAIN TRANSITION PROBABILITIES
============================================================

                Next Character Type
              ┌─────────┬───────────┐
              │  Vowel  │ Consonant │
┌─────────────┼─────────┼───────────┤
│ Vowel       │  0.3542 │   0.6458  │
│ Consonant   │  0.4123 │   0.5877  │
└─────────────┴─────────┴───────────┘

Raw Transition Counts:
  Vowel -> Vowel: 153 (out of 432)
  Vowel -> Consonant: 279 (out of 432)
  Consonant -> Vowel: 245 (out of 594)
  Consonant -> Consonant: 349 (out of 594)

============================================================
ACCURACY TEST
============================================================

Predictions: 628 correct out of 1026 total
Accuracy: 61.21%

============================================================
SUMMARY STATISTICS
============================================================
Total characters analyzed: 1337
Alphabetic characters: 1027
  Vowels: 433 (42.2%)
  Consonants: 594 (57.8%)
Total transitions tracked: 1026
```

## How It Works

1. **Text Loading**: The script loads text either from a file or a variable
2. **Character Classification**: Each alphabetic character is classified as vowel or consonant
3. **Transition Tracking**: The script counts how many times each transition type occurs
4. **Probability Calculation**: Counts are converted to probabilities
5. **Chain Display**: The transition probabilities are displayed in a formatted table
6. **Accuracy Testing**: The model predicts each character type and compares to actual values
7. **Results**: Statistics and accuracy metrics are displayed

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Understanding the Results

### Transition Probabilities

The probability matrix shows the likelihood of each transition:
- Values closer to 1.0 indicate high probability
- Values closer to 0.0 indicate low probability
- Each row sums to 1.0

### Typical Accuracy

For English text, accuracy typically ranges from **55-70%** because:
- English has patterns (consonant clusters, vowel patterns)
- The model only considers the immediate previous character
- Some transitions are more predictable than others

Low accuracy (< 50%) might indicate:
- Very short text sample
- Unusual text patterns
- Text in a non-English language with different phonetic rules

High accuracy (> 70%) might indicate:
- Very regular patterns in the text
- Repetitive content
- Specific vocabulary that follows strong phonetic patterns