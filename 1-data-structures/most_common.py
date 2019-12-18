from collections import Counter

def main():
    words = [
        'look', 'into', 'my', 'eyes', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes'
    ]

    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

if __name__ == "__main__":
    main()