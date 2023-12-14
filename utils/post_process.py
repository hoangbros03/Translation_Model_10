"""
Post process translated file and original pre-tokenized file.
"""
import logging
import re
import argparse

from underthesea import text_normalize

def post_process(sentence):
    sentence = re.sub(r"𐇛+"," ", sentence)
    sentence = text_normalize(sentence)
    sentence = re.sub(
    r"[\*\"“”\n\\…\+\-\/\=\(\)‘•:\[\]\|’\!;]", " ", str(sentence))
    sentence = re.sub(r"[ ]+", " ", sentence)
    sentence = re.sub(r"\!+", "!", sentence)
    sentence = re.sub(r"\,+", ",", sentence)
    sentence = re.sub(r"\?+", "?", sentence)
    sentence = re.sub(r"\?+", "?", sentence)
    if sentence[-1] not in [".", "?", "!"]:
        sentence = sentence + " ."
    # sentence = sentence + "\n"
    return sentence

def process(input_path, output_path):
    with open(input_path,"r") as f:
        data = f.readlines()
    print(f"Total sentences: {len(data)}")
    with open(output_path,"a") as f:
        for idx, sent in enumerate(data):
            f.write(post_process(sent))
            if idx < len(data) - 1:
                f.write("\n")
    print("Completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file", type=str, required=True)
    parser.add_argument("--output", help="Output file", type=str, required= True)
    args = parser.parse_args()
    process(args.input, args.output)