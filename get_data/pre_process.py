"""
File to process and get the data file of language B from data file of language A
Input:
    Directory of file of language A
    Language A
    Language B
Output:
    New data file of language A
    New data file of language B
"""
import logging
import argparse
import re

from googletrans import Translator

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def process(input_path, output_src, output_target, src_lang, dest_lang):
    # TODO: Add pre-processing to eliminate symbols + strip + try catch
    # TODO: Handle many sentence together
    MIN_CHARACTER=30
    MAX_CHARACTER=600
    with open(input_path, "r") as f:
        src_lst = f.readlines()
    new_src = []
    new_tgt = []
    translator = Translator()
    for idx, sentence in enumerate(src_lst):
        if len(sentence) > MAX_CHARACTER or len(sentence) < MIN_CHARACTER:
            continue
        new_src.append(sentence)
        new_tgt.append(translator.translate(sentence,src=src_lang, dest=dest_lang))
        if (idx+1)%(max(len(src_lst)//10,1))==0:
            logging.info(f"Processed {idx+1}/{len(src_lst)}")
    with open(output_src, "w") as f:
        for it in new_src:
            f.write(it)
    with open(output_target, "w") as f:
        for it in new_tgt:
            f.write(f"{it.text}\n")
    logging.info("Completed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_path", help='Input file path', type=str, required=True)
    parser.add_argument("-os","--output_src", help='Output source file path', type=str, required=True)
    parser.add_argument("-ot","--output_target", help='Output target file path', type=str, required=True)
    parser.add_argument("-s","--src_lang", help='Source language', type=str, default="vi")
    parser.add_argument("-d","--dest_lang", help='Destination language', type=str, default='lo')
    args = parser.parse_args()
    process(
        args.input_path,
        args.output_src,
        args.output_target,
        args.src_lang,
        args.dest_lang
    )