"""
Update: Since Google API doesn't allow us to abusing their system,
we will translate in a manual but the only way!
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

def process(input_path, output_src, output_target, src_lang, dest_lang, trans_type="group", step=30, it_start = 0):
    # For weird reason, step will not be exceed 30!
    step = min(30,step)
    
    MIN_WORD=2
    MAX_WORD=200
    with open(input_path, "r") as f:
        src_lst = f.readlines()
    new_src = []
    new_tgt = []
    translator = Translator()
    if trans_type=="group":
        sentence_it = it_start
        while sentence_it < len(src_lst):
        # for sentence_it in range(0, len(src_lst), step):
            # standard_src_lst = [sentence.replace('.', '') for sentence in src_lst[sentence_it:min(len(src_lst), sentence_it+step)]]
            concat_sentence = " ".join(src_lst[sentence_it:min(len(src_lst), sentence_it+step)])
            # print(type(concat_sentence))
            # concat_sentence = concat_sentence.replace('\n', '')
            # print(f"{sentence_it}:{min(len(src_lst), sentence_it+step)}")
            try:
                trans_concat_sentence = translator.translate(concat_sentence,src=src_lang, dest=dest_lang).text
            except Exception as e:
                logging.info("Maybe read time out, however we will try again...")
                continue
            trans_translate = re.split('\n', trans_concat_sentence)
            # Check if num of sentence is equal
            # print(f"Offset: {len(trans_translate) - (min(len(src_lst), sentence_it+step) - sentence_it)}")
            if len(trans_translate) != min(len(src_lst), sentence_it+step) - sentence_it:
                sentence_it += step
                continue
            else:
                trans_translate = [sentence.replace('\n', '').strip() for sentence in trans_translate if sentence.strip()]
                new_src.extend(src_lst[sentence_it:min(len(src_lst), sentence_it+step)])
                new_tgt.extend(trans_translate)
                if (sentence_it+1)%(max(len(src_lst)//10,1))==0:
                    logging.info(f"Processed {sentence_it+1}/{len(src_lst)}")
                sentence_it += step
                
    elif trans_type=="separate":
        for idx, sentence in enumerate(src_lst):
            if len(sentence.split(" ")) > MAX_WORD or len(sentence.split(" ")) < MIN_WORD:
                continue
            new_src.append(sentence)
            try:
                new_tgt.append(translator.translate(sentence,src=src_lang, dest=dest_lang).text)
            except Exception as e:
                continue
            if (idx+1)%(max(len(src_lst)//10,1))==0:
                logging.info(f"Processed {idx+1}/{len(src_lst)}")
    else:
        raise ValueError("Wrong trans_type!")
    with open(output_src, "w") as f:
        for it in new_src:
            f.write(it)
    with open(output_target, "w") as f:
        for it in new_tgt:
            f.write(f"{it}\n")
    logging.info("Completed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_path", help='Input file path', type=str, required=True)
    parser.add_argument("-os","--output_src", help='Output source file path', type=str, required=True)
    parser.add_argument("-ot","--output_target", help='Output target file path', type=str, required=True)
    parser.add_argument("-s","--src_lang", help='Source language', type=str, default="vi")
    parser.add_argument("-d","--dest_lang", help='Destination language', type=str, default='lo')
    parser.add_argument("--step", help='step if translate by group', type=int, default=80)
    parser.add_argument("-t","--trans_type", help='Type of translate (group | separate)', type=str, default='group')
    parser.add_argument("-si","--start_index", help='Start index of sentence inside file to translate', type=int, default=0)

    args = parser.parse_args()
    process(
        args.input_path,
        args.output_src,
        args.output_target,
        args.src_lang,
        args.dest_lang,
        args.trans_type,
        args.step,
        args.start_index
    )