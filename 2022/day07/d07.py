
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


DISK_SPACE = 70000000
REQUIRED_SPACE = 30000000

size_dirs_less_10k = 0
size_removed_file = DISK_SPACE


class Directory:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.subdirs = []
        self.files = []

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)
        subdir.parent = self

    def add_file(self, file):
        self.files.append(file)

    def cd(self, path):
        if path == '..':
            return self.parent

        for dir in self.subdirs:
            if dir.name == path:
                return dir

    def size(self, threshold=DISK_SPACE):
        size = 0
        global size_dirs_less_10k, size_removed_file

        for file in self.files:
            size += file.size

        for dir in self.subdirs:
            size += dir.size(threshold)

        if size <= 100000:
            size_dirs_less_10k += size

        if size >= threshold and self.parent != None:
            size_removed_file = min(size_removed_file, size)
        return size


with open('07_example.txt') as input:
    commands = [line.strip() for line in input.readlines()][1:]

cur = root = Directory('/')

for command in commands:
    if command.startswith('$ cd'):
        cur = cur.cd(command[5:])
    elif command.startswith('dir'):
        cur.add_subdir(Directory(command[4:]))
    elif command.startswith('$ ls'):
        continue
    else:
        size, name = command.split(' ')
        cur.add_file(File(name, int(size)))


used_space = root.size()
print("Part 1 answer:", size_dirs_less_10k)
free_space = DISK_SPACE - used_space
root.size(REQUIRED_SPACE - free_space)
print("Part 2 answer: ", size_removed_file)
