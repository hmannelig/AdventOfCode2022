class File:
    __name: str = None
    __size: int = 0

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def set_file_name(self, name: str):
        self.__name = name

    def set_file_size(self, size: int):
        self.__size = size

    def get_file_name(self) -> str:
        return self.__name

    def get_file_size(self) -> str:
        return self.__size
