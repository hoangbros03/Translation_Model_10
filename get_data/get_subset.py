""" 
Get subset from a dataset, allow to train and track model on smaller scale.
Not support argparse since I don't have time.
"""
import random

def choose_random_lines(input1, input2, num_lines=10):
    """
    Input1 and input2 must have the same lines number and consistency.
    """
    with open(input1, 'r') as file1, open(input2, "r") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    # Make sure the number of requested lines is not greater than the total number of lines in the file
    num_lines = min(num_lines, len(lines1))
    random_numbers = random.sample(range(len(lines1)), num_lines)

    # Write chosen lines to the output file
    with open(f"{input1[:-3]}_subset.{input1[-2:]}", 'w') as file1, \
    open(f"{input2[:-3]}_subset.{input2[-2:]}", 'w') as file2:
        for i, line_idx in enumerate(random_numbers):
            if i==len(random_numbers)-1:
                file1.write(lines1[line_idx][:-1])
                file2.write(lines2[line_idx][:-1])
            else:
                file1.write(lines1[line_idx])
                file2.write(lines2[line_idx])
    print("Completed!")
    
if __name__=="__main__":
    # Make change here
    choose_random_lines(
        '../data/nlp_lovi_data/train_processed.lo',
        '../data/nlp_lovi_data/train_processed.vi',
        num_lines=10)