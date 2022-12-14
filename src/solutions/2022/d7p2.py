from typing import Dict

from utils import run, ParsingConfig


example_answer = 24933642

example_data = """
$ cd /
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
7214296 k
"""


class Sizer:
    def __init__(self):
        self.cwd = []
        self.tree: Dict[str, Dir] = {}
        self.ls_dir = None

    def parse(self, *line):
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    self.cwd.pop()
                else:
                    self.cwd.append(line[2])
            else:
                dirname = "/".join(self.cwd)
                self.ls_dir = Dir(dirname)
                self.tree[dirname] = self.ls_dir
        else:
            if line[0] == "dir":
                self.ls_dir.add_subdir(line[1])
            else:
                self.ls_dir.add_file(int(line[0]))

    def fix_sizes(self):
        while True:
            pending = [d for d in self.tree.values() if d.unknown_size_subdirs]
            if not pending:
                return

            for p in pending:
                for u in p.unknown_size_subdirs.copy():
                    subdir = self.tree[f"{p.name}/{u}"]
                    if not subdir.unknown_size_subdirs:
                        p.add_file(subdir.file_size)
                        p.unknown_size_subdirs.remove(u)


class Dir:
    def __init__(self, dirname):
        self.name = dirname
        self.subdirs = []
        self.file_size = 0
        self.unknown_size_subdirs = []

    def add_file(self, size):
        self.file_size += size

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)
        self.unknown_size_subdirs.append(subdir)


parsing_config = ParsingConfig(
    parser_class=Sizer,
)


def solve(sizer: Sizer):
    sizer.fix_sizes()
    root_size = sizer.tree["/"].file_size
    available_size = 70000000 - root_size
    needed_size = 30000000 - available_size
    best_dir = min(d.file_size for d in sizer.tree.values() if d.file_size >= needed_size)
    return best_dir


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
