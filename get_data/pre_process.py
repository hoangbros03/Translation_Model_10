"""
Preprocess the data from .lo and .vi file
"""
import re
import argparse

reg = r'\(?[A-Za-z0-9\u0e80-\u0effaAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ]+\)?[.!?,:]?'
def process(input_file, output_file):
    result = []
    process_code = re.compile(reg, re.UNICODE)
    with open(input_file, "r") as f:
        data = f.readlines()
    print(f"Total sentences: {len(data)}")
    with open(output_file,"a") as f:
        for i, d in enumerate(data):
            f.write(" ".join(process_code.findall(d)))
            if i < len(data)-1:
                f.write("\n")
    print("Completed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",help="input file", type=str, required=True)
    parser.add_argument("-o","--output",help="output file", type=str, required=True)
    args = parser.parse_args()
    process(args.input, args.output)
