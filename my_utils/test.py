# from str_util import *
import my_utils.str_util
import my_utils.file_util

reverse = my_utils.str_util.str_reverse("黑娘程序猿")
substr = my_utils.str_util.substr("发裂缝哈黑发", 0, 4)

print(reverse)
print(substr)

my_utils.file_util.print_file_info("D:\last.txt")
my_utils.file_util.append_to_file("D:\last.txt", "哎哈哈哈\n")
