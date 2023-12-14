"""
Pre-tokenize the data, since there is a problem
when implement tokenize inside.
"""
from underthesea import word_tokenize as vi_word_tokenize
from laonlp.tokenize import word_tokenize as lo_word_tokenize

def pre_tokenize(i1, i2, o1, o2):
    with open(i1, "r") as f:
        lo_st = f.readlines()
    with open(i2, "r") as f:
        vi_st = f.readlines()
    with open(o1, "w") as f:
        for i, st in enumerate(lo_st):
            f.write("𐇛".join(lo_word_tokenize(st)))
            if (i+1)%10000==0:
                print(f"Ok with {i+1}/{len(lo_st)}")
    with open(o2, "w") as f:
        for i, st in enumerate(vi_st):
            f.write("𐇛".join(vi_word_tokenize(st)))
            if i < len(vi_st)-1:
                f.write("\n")
            if (i+1)%10000==0:
                print(f"Ok with {i+1}/{len(lo_st)}")

if __name__=="__main__":
    # Make change here
    i1 ="" # Input file lo
    i2 ="" # Input file vi
    o1 ="" # Output file lo
    o2 ="" # Output file vi
    pre_tokenize(i1, i2, o1, o2)
