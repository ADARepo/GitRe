import random, os, sys

TEXT_DIR = "../text_files"
if not os.path.exists(TEXT_DIR):
    os.mkdir(TEXT_DIR)

NUM_PHONE_NUMS = 10000000

def gen_phone_nums():
    '''
        Will write to phone_num_file NUM_PHONE_NUMS newline separated phone numbers (US).
    '''

    # Relative location to the file we want to write to.
    phone_num_file = "/numbers.txt"
    phone_num_loc = os.path.relpath(TEXT_DIR + phone_num_file)

    # Length does not include '-'s.
    phone_num_len = 12

    random.seed()

    list_nums = [''] * NUM_PHONE_NUMS

    # For each phone number, generate 10 digit phone number with hyphens, non-zero starting digit.
    # This is significantly faster than appending single random digits to string and inserting hyphens at correct spot...
    # at least the way I had tried it. 10 million #s ~12 seconds this way, ~45 seconds one at a time.
    for i in range(NUM_PHONE_NUMS):
        num_list = list(str(random.randrange(100000000000,999999999999)))
        num_list[3] = '-'
        num_list[7] = '-'

        list_nums[i] = "".join(num_list)

    with open(phone_num_loc, 'w') as file:
        for num in list_nums:
            file.write(num)
            file.write('\n')

if __name__ == "__main__":
    # Change working dir to scripts location for relative path to work.
    file_path = os.path.abspath(sys.argv[0])
    file_dir_path = os.path.dirname(file_path)
    os.chdir(file_dir_path)

    gen_phone_nums()