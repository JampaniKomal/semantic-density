import urllib.request
import math
import matplotlib.pyplot as plt
import os

def calculate_P(L):
    """
    P(L) represents the total number of possible suffixes of length up to L.
    This calculates exactly how many strings can exist within a given remaining length constraint.
    """
    return (26**(L + 1) - 1) // 25

def get_absolute_index(word, M, P_cache):
    """
    Mathematically computes the absolute lexicographical index of a word 
    within the total theoretical combinatorial space of max length M,
    without needing to generate the combinations.
    """
    index = 0
    for i, char in enumerate(word):
        remaining_L = M - (i + 1)
        char_val = ord(char) - ord('a')
        
        # Add the skipped subtrees
        index += char_val * P_cache[remaining_L]
        # Add the word itself at this node
        index += 1
    return index

def run_analysis():
    print("1. Downloading dictionary dataset...")
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8').splitlines()
    
    print("2. Parsing and cleaning data...")
    meaningful_words = []
    for w in data:
        w = w.strip().lower()
        if w.isalpha():
            meaningful_words.append(w)
            
    # Sort alphabetically to get Meaningful Index
    meaningful_words.sort()
    meaningful_words = list(dict.fromkeys(meaningful_words)) # remove duplicates
    
    M = max(len(w) for w in meaningful_words)
    longest_word = [w for w in meaningful_words if len(w) == M][0]
    print(f"   Max length (M) = {M}")
    print(f"   Longest word = {longest_word}")
    print(f"   Total valid words = {len(meaningful_words)}")
    
    print("3. Precomputing combinatorial suffix trees...")
    P_cache = {L: calculate_P(L) for L in range(M + 1)}
    
    total_space = calculate_P(M) - 1
    print(f"   Total theoretical space size = {total_space} (~10^{math.log10(total_space):.1f})")
    
    print("4. Computing absolute combinatorial indices...")
    x_meaningful = []
    y_absolute_log = []
    
    for meaningful_index, word in enumerate(meaningful_words, start=1):
        abs_idx = get_absolute_index(word, M, P_cache)
        
        x_meaningful.append(meaningful_index)
        # We must use log10 because the absolute index reaches up to 10^43
        y_absolute_log.append(math.log10(abs_idx) if abs_idx > 0 else 0)
        
    print("5. Plotting Semantic Density Curve...")
    plt.figure(figsize=(12, 7))
    plt.plot(x_meaningful, y_absolute_log, color='#2c3e50', linewidth=2)
    
    plt.title("Semantic Density in Combinatorial Space", fontsize=16, fontweight='bold')
    plt.xlabel("Dictionary Index (Relative Human Meaning)", fontsize=12)
    plt.ylabel("Log10(Absolute Index) (Theoretical Mathematical Void)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Add annotations
    plt.annotate(f"Dictionary Size: {len(meaningful_words):,} words\nCombinatorial Space: ~10^{math.log10(total_space):.1f}", 
                 xy=(len(meaningful_words)*0.05, 40),
                 fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="#ecf0f1", ec="#2c3e50", lw=1))
                 
    output_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(output_dir, "semantic_density_curve.png")
    plt.savefig(image_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to {image_path}")

if __name__ == "__main__":
    run_analysis()
