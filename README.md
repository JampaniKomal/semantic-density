# Semantic Density in Combinatorial Space

This repository contains a mathematical and linguistic experiment that maps the entire English dictionary into the theoretical absolute void of all possible character combinations.

## The Experiment

In computational linguistics, we often deal with strings of characters. If we take an alphabet of 26 letters and a maximum string length of 31 (the length of the longest purely alphabetical English word, `dichlorodiphenyltrichloroethane`), there are mathematically **7.6 × 10⁴³** possible combinations of letters.

Generating all combinations is physically impossible, as this number is significantly larger than the number of stars in the observable universe. However, we can use a pure mathematical approach (via 26-ary combinatorial suffix trees) to calculate the *exact Absolute Lexicographical Index* of any human word within that theoretical void, without ever having to generate the void itself.

## The Findings

By plotting the **Relative Dictionary Index** (1 to ~370,000 human words) against the **Absolute Mathematical Index** (1 to 10⁴³) on a logarithmic scale, we visualize the structure of semantic meaning.

![Semantic Density Curve](semantic_density_curve.png)

The resulting curve is remarkably linear on a logarithmic scale. This demonstrates that human language expands into combinatorial space exponentially and predictably. The subtle "wobbles" or steps in the curve represent gravitational anomalies in language: human biases towards certain highly common prefixes (like `re-` or `con-`) that cluster thousands of words tightly together while leaving vast mathematical voids of unused permutations nearby.

## Running the Analysis

Requires Python 3 and `matplotlib`.

```bash
pip install matplotlib
python semantic_density.py
```

This will automatically download the English dictionary dataset, compute the absolute combinatorial indices for all ~370,000 words, and generate the semantic density plot.
