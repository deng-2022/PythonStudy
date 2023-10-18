#
def print_file_info(file_name):
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except Exception as e:
        print(f"{e}  报错了!")
    else:
        for line in f:
            print(f"{line}\n")
    finally:
        print("真不戳")


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.flush()
    print("真不戳呢")


if __name__ == '__main__':
    print_file_info("D:\last.txt")
    append_to_file("D:\last.txt", "??????????????????\n")
