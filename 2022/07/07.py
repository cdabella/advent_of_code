from aocd import data, lines, submit

import re

cmd_start = "$"
cd = "$ cd"
cd_up = ".."
cd_root = "/"

ls = "$ ls"
dir_file = "dir"


class Directory:
    def __init__(self, name, parent, files=[], child_dirs={}):
        self.name = name
        self.parent = parent
        self.files = files
        self.child_dirs = child_dirs
        self.file_size = 0
        self.total_size = 0

    def __repr__(self):
        return str({"name": self.name, "parent": self.parent.name})


def filter_dir_by_size(dir: Directory, filter_size=100000):
    subdirs_total_size = 0
    matching_dirs = []
    for child_dir in dir.child_dirs.values():
        subdir_size, matching_subdirs = filter_dir_by_size(child_dir, filter_size)
        matching_dirs.extend(matching_subdirs)
        subdirs_total_size += subdir_size
    total_size = subdirs_total_size + dir.file_size
    dir.total_size = total_size
    if total_size <= filter_size:
        matching_dirs.append((dir.name, total_size))
    return total_size, matching_dirs


# lines = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".split(
#     "\n"
# )


def pt1():
    root_dir = Directory(name="/", parent="/")
    root_dir.parent = root_dir
    current_dir = root_dir
    idx = 1  # skip "cd /"
    while idx < len(lines):
        input = lines[idx]
        cmd = input[:4]
        args = input[5:]  # skip space
        if cmd == cd:
            if args == cd_up:
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.child_dirs[args]
            idx += 1
        elif cmd == ls:
            files = []
            child_dirs = {}
            idx += 1
            size = 0
            while idx < len(lines) and lines[idx][0] != cmd_start:
                if lines[idx][:3] == dir_file:
                    child_dir_name = lines[idx].split()[1]
                    child_dir = Directory(name=child_dir_name, parent=current_dir)
                    child_dirs[child_dir_name] = child_dir
                elif lines[idx][:3] != dir_file:
                    # if current_dir.name == "gdqqtvnp":
                    #     breakpoint()
                    file_size, file_name = tuple(lines[idx].split())
                    file_size = int(file_size)
                    files.append((file_size, file_name))
                    size += file_size
                idx += 1
            current_dir.files = files
            current_dir.child_dirs = child_dirs
            current_dir.file_size = size

    _, matching_dirs = filter_dir_by_size(root_dir)
    total = sum([dir[1] for dir in matching_dirs])
    print(total)
    # submit(total)
    return root_dir


def list_all_dir_sizes(dir: Directory):
    sizes = [dir.total_size]
    for child_dir in dir.child_dirs.values():
        child_dir_sizes = list_all_dir_sizes(child_dir)
        sizes.extend(child_dir_sizes)
    return sizes


def pt2(root_dir):
    total_space = 70000000
    unused_space_target = 30000000
    unused_space = total_space - root_dir.total_size
    delete_size = unused_space_target - unused_space
    answer = sorted(
        [size for size in list_all_dir_sizes(root_dir) if size > delete_size]
    )[0]
    print(answer)
    # submit(answer)


if __name__ == "__main__":
    root_dir = pt1()
    pt2(root_dir)
