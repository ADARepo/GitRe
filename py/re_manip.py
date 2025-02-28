import re
import random
import os
import sys

class Re_Factory:
    def run_in_script_dir():
        '''
            Change to script's location for correct relative location to text files.
            Also creates text_files directory.
        '''
        file_path = os.path.abspath(sys.argv[0])
        file_dir_path = os.path.dirname(file_path)
        os.chdir(file_dir_path)

        text_dir = "../text_files"
        if not os.path.exists(text_dir):
            os.mkdir(text_dir)

    def gen_phone_nums(num_nums = 10000000):
        '''
            Will write to phone_num_file num_nums newline separated phone numbers (US).
            num_nums        number of phone numbers to write to file, default 10000000.
        '''

        # Relative location to the file we want to write to.
        phone_num_file = "/numbers.txt"
        phone_num_loc = os.path.relpath(TEXT_DIR + phone_num_file)

        # Length does include '-'s.
        phone_num_len = 12

        random.seed()

        list_nums = [''] * num_nums

        # For each phone number, generate 10 digit phone number with hyphens, non-zero starting digit.
        for i in range(num_nums):
            num_list = list(str(random.randrange(100000000000,999999999999)))
            num_list[3] = '-'
            num_list[7] = '-'

            list_nums[i] = "".join(num_list)

        with open(phone_num_loc, 'w') as file:
            for num in list_nums:
                file.write(num)
                file.write('\n')

    def ret_list_match(pttrn, file_to_search):
        '''
            Searches through file_to_search with given pattern. Returns list of matches with re.finditer.
            pttrn               pattern to use with re.
            file_to_search      file to look through with pattern.
        '''
        compiled_pttrn = re.compile(pttrn)

if __name__ == "__main__":
    ref = Re_Factory

    ref.run_in_script_dir()