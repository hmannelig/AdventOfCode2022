import File


class Directory:
    __dir_name: str = None
    __folders, __files = None, None
    __parent_dir = None

    def __init__(self, dir_name: str, parent_dir):
        self.__dir_name = dir_name
        self.__parent_dir = parent_dir
        self.__folders = []
        self.__files = []

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

    def set_dir_name(self, name):
        self.__dir_name = name

    def contains_file(self, file_name: str):

        for f in self.__files:
            if f.get_file_name() == file_name:
                return True

        return False

    def add_file(self, f: File):
        self.__files.append(f)

    def get_folders(self):
        return self.__folders
