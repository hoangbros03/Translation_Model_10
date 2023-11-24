import logging
import argparse

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def process(input_files, output_file):
    for file in input_files:
        try:
            with open(file, "r") as f1, open(output_file, "a") as f2:
                f2.write("".join(f1.readlines()))

        except Exception as e:
            logging.info(f"Error: {e}")
            logging.info("Process will continue...")
            continue
    logging.info("Completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', type=str, nargs='+',
                        help='list of files')
    parser.add_argument("-o", "--output", type=str, help="output file name", default="output_merge.txt")
    args = parser.parse_args()
    process(args.files, args.output)