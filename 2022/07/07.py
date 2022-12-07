from aocd import data, lines, submit

import re

cmd_start = "$"
cd = "$ cd"
cd_up = ".."
cd_root = "/"

ls = "$ ls"
dir_file = "dir"


class Directory:
    def __init__(self, name, parent, files=[], dirs=[]):
        self.name = name
        self.parent = parent
        self.files = files
        self.dirs = dirs
        self.size = 0

    def __repr__(self):
        return str({"name": self.name, "parent": self.parent.name})


def parse_dir(dir: Directory, filter_size=100000):
    subdirs_total_size = 0
    matching_dirs = []
    for child_dir in dir.dirs:
        subdir_size, matching_subdirs = parse_dir(child_dir)

        subdirs_total_size += subdir_size
    total_size = subdirs_total_size + dir.size


lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split(
    "\n"
)


def pt1():
    dirs = {}
    current_dir = Directory(name="/", parent="/")
    idx = 0
    while idx < len(lines):
        input = lines[idx]
        cmd = input[:4]
        args = input[5:]  # skip space
        if cmd == cd:
            if args == cd_up:
                current_dir = current_dir.parent
            else:
                current_dir = dirs.get(args, Directory(name=args, parent=current_dir))
                dirs[args] = current_dir
            idx += 1
        elif cmd == ls:
            files = []
            child_dirs = []
            idx += 1
            size = 0
            while idx < len(lines) and lines[idx][0] != cmd_start:
                if lines[idx][:3] == dir_file:
                    child_dir_name = lines[idx].split()[1]
                    child_dir = dirs.get(
                        child_dir_name,
                        Directory(name=child_dir_name, parent=current_dir),
                    )
                    child_dirs.append(child_dir)
                if lines[idx][:3] != dir_file:
                    file_size, file_name = tuple(lines[idx].split())
                    file_size = int(file_size)
                    files.append((file_size, file_name))
                    size += file_size
                idx += 1
            print(current_dir.name, files, child_dirs)
            current_dir.files = files
            current_dir.dirs = child_dirs
            current_dir.size = size
    print(dirs)
    print(parse_dir(dirs["/"]))


def pt2():
    pass


if __name__ == "__main__":
    pt1()
    # pt2()
