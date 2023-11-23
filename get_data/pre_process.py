"""
Preprocess the data from .lo and .vi file
"""
import re
import argparse

# Regex of both .lo and .vi file
reg = r'\(?[A-Za-z0-9\u0e80-\u0effaAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ]+\)?[.!?,:]?'
def process(input_src, input_tgt, output_source, output_target, max_len):
    result = []
    process_code = re.compile(reg, re.UNICODE)
    with open(input_src, "r") as file1, open(input_tgt, "r") as file2:
        data1 = file1.readlines()
        data2 = file2.readlines()
    print(f"Total sentences: {len(data1)}")
    with open(output_source,"w") as file1, open(output_target,"w") as file2:

        for idx in range(len(data1)):
            """
            Trying to detect if more than max_len word -> discard
            """
            if max(len(data1[idx].split(" ")), len(data2[idx].split(" "))) > max_len:
                continue
            else:
                file1.write(" ".join(process_code.findall(data1[idx])))
                if idx < len(data1)-1:
                    file1.write("\n")
                file2.write(" ".join(process_code.findall(data2[idx])))
                if idx < len(data2)-1:
                    file2.write("\n")
    print("Completed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-is","--input_source",help="input source file (.lo file)", type=str, required=True)
    parser.add_argument("-it","--input_target",help="input target file (.vi file)", type=str, required=True)
    parser.add_argument("-os","--output_source",help="output source file", type=str, required=True)
    parser.add_argument("-ot","--output_target",help="output target file", type=str, required=True)
    parser.add_argument("--max_len", help="max len of sentence", type=int, default=180)
    args = parser.parse_args()
    process(args.input_source, args.input_target, args.output_source, args.output_target, args.max_len)
