file = open('no_space_left_on_device').read().splitlines()


class File:
    __name: str = None
    __size: int = 0

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_file_name(self) -> str:
        return self.__name

    def get_file_size(self) -> str:
        return self.__size


class Directory:
    __dir_name: str = None
    __folders, __files, __parent_dir = None, None, None

    def __init__(self, dir_name: str, parent_dir):
        self.__dir_name = dir_name
        self.__parent_dir = parent_dir
        self.__folders, self.__files = [], []

    def get_size(self) -> int:
        return self.__get_folders_size() + self.__get_files_size()

    def __get_folders_size(self) -> int:

        if len(self.__folders) == 0:
            return 0

        total_size = 0
        for folder in self.__folders:
            total_size += folder.get_size()

        return total_size

    def __get_files_size(self) -> int:

        if len(self.__files) == 0:
            return 0

        total_size = 0
        for f in self.__files:
            total_size += f.get_file_size()

        return total_size

    def get_contents(self) -> str:
        content = ''
        for fol in self.__folders:
            content += fol.get_dir_name() + '\n'

        for f in self.__files:
            content += f.get_file_name() + '\n'

        return content

    def add_dir(self, dir):

        if not self.contains_dir(dir.get_dir_name()):
            self.__folders.append(dir)

    def contains_dir(self, dir_name) -> bool:
        for fol in self.__folders:

            if fol.get_dir_name() == dir_name:
                return True

        return False

    def get_dir(self, dir_name):

        for fol in self.__folders:
            if fol.get_dir_name() == dir_name:
                return fol

        pass

    def get_parent_dir(self):

        if self.__parent_dir is None:
            return self

        return self.__parent_dir

    def get_dir_name(self) -> str:
        return self.__dir_name

    def contains_file(self, file_name: str):

        for f in self.__files:
            if f.get_file_name() == file_name:
                return True

        return False

    def add_file(self, f: File):

        if not self.contains_file(f.get_file_name()):
            self.__files.append(f)

    def get_folders(self):
        return self.__folders


root_dir: Directory = Directory('/', None)

for line in file:
    line = line.split(' ')

    if line[0] == '$' and line[1] == 'cd':

        if line[2] == '..':
            print('Going back one directory from', root_dir.get_dir_name(), 'to',
                  root_dir.get_parent_dir().get_dir_name())
            root_dir = root_dir.get_parent_dir()

        elif line[2] != root_dir.get_dir_name():

            if not root_dir.contains_dir(line[2]):
                print('Creating new directory', line[2], 'in', root_dir.get_dir_name())

                new_dir: Directory = Directory(line[2], root_dir)
                root_dir.add_dir(new_dir)
                root_dir = new_dir
                print('Moved to newly created directory', new_dir.get_dir_name())

            else:
                print('Moving from current directory', root_dir.get_dir_name(), 'to directory', line[2])
                root_dir = root_dir.get_dir(line[2])

    elif line[0].isnumeric() and not root_dir.contains_file(line[1]):
        print('Adding new file', line[1], 'to', root_dir.get_dir_name())
        new_file: File = File(line[1], int(line[0]))
        root_dir.add_file(new_file)

while root_dir.get_dir_name() != '/':
    root_dir = root_dir.get_parent_dir()

print(root_dir.get_dir_name())
print(root_dir.get_contents())
print(root_dir.get_size())
