import re
import random
import os
import sys

class Re_Factory:

    TEXT_DIR = r"..\text_files"

    PHONE_NUM_FILE = "numbers.txt"

    TEXT_FILES = [PHONE_NUM_FILE]

    def run_in_script_dir(self):
        '''
            Change to script's location for correct relative location to TEXT_DIR.

            Also creates TEXT_DIR directory.
        '''
        file_path = os.path.abspath(sys.argv[0])
        file_dir_path = os.path.dirname(file_path)
        os.chdir(file_dir_path)

        if not os.path.exists(self.TEXT_DIR):
            os.mkdir(self.TEXT_DIR)
    

    def gen_phone_nums(self, num_nums = 10000000):
        '''
            Will write to PHONE_NUM_FILE num_nums newline separated phone numbers (US).

            num_nums        number of phone numbers to write to file, default 10000000.
        '''

        num_file = os.path.join(self.TEXT_DIR, self.PHONE_NUM_FILE)

        if not os.path.exists(num_file):
            with open(num_file, 'w') as file:
                pass

        # Length includes '-'s.
        phone_num_len = 12

        random.seed()

        list_nums = [''] * num_nums

        # For each phone number, generate 10 digit phone number with hyphens, non-zero starting digit.
        for i in range(num_nums):
            num_list = list(str(random.randrange(100000000000,999999999999)))
            num_list[3] = '-'
            num_list[7] = '-'

            list_nums[i] = "".join(num_list)

        with open(num_file, 'w') as file:
            for num in list_nums:
                file.write(num)
                file.write('\n')

    def ret_list_match(self, pttrn, file_to_search):
        '''
            Searches through file_to_search with given pattern. Returns list of matches with re.findall.
            File must be inside of TEXT_DIR directory.

            pttrn               pattern to use with re.
            file_to_search      file to look through with pattern.
        '''
        file_loc = self.TEXT_DIR + f"/{file_to_search}"

        if not os.path.exists(file_loc):
            sys.stdout.write(f"{file_to_search} was not found.")
            return None

        compiled_pttrn = re.compile(pttrn)

        with open(file_loc, 'r') as file:
            text = file.read()
        
        match_list = compiled_pttrn.findall(text)

        return match_list

if __name__ == "__main__":
    ref = Re_Factory()

    ref.run_in_script_dir()
    matches = ref.ret_list_match(r'5\d\d-\d{3}-\d{3}5', ref.PHONE_NUM_FILE)

    print(len(matches))
    print(f"{len(matches)/10000000 * 100.0:.2}% ")
