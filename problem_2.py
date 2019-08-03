# os.path.isdir(path)
#
# os.path.isfile(path)
#
# os.listdir(directory)
#
# os.path.join(...)
class file:
    def __init__(self):
        self.list = []

    def display(self):
        if len(self.list) == 0:
            print("Sorry no extension provided or found")
        for i in self.list:
            print(i)

    def find_files(self,suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
        """
        list = []
        if not os.path.isdir(path) or os.path.islink(path):
            print("No path provided")
            return

        for entry in os.scandir(path):
            if entry.is_dir():
                # if the the current state of the path is a directory then call find_files again
                self.find_files(suffix,entry)
            elif entry.is_file():
                # if the current state of the path is a file then check the extension of the file to see if it matches with "c"
                if entry.path.endswith(suffix):
                    #  if the file extension matches with the suffix the print the file
                    # print (entry.path)
                    self.list.append(entry.path)
            # elif not entry.is_file() or not extry.exists():
            #     raise NameError("No extension provided")
            elif not os.path.isfile(path):
                print("No extension or file provided")


import os

path = "./testdir"
list = file()
list.find_files("c",path)
list.display()

path2 = "./tesdir"
list_2 = file()
list_2.find_files("c", path2)

path3 = "./testdir"
list_3 = file()
list_3.find_files("ss",path3)
list_3.display()
# for i in list:
#     print(i)
