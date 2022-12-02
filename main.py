import os

def changeFileNames():
    print("Enter the full file path: ")
    filepath = input()
    file_list = os.listdir(filepath)
    print("Enter prefix [leave blank for 0..n]: ")
    prefix = input()
    print("Enter staring index [leave blank for 0]: ")
    starting_index = input()

    for idx, f in enumerate(file_list):
        if starting_index != "":
            idx = idx + int(starting_index)
        ext = f.split(".")[-1]
        old_name = filepath + "/" + f
        if prefix != "":
            new_name = filepath + "/" + prefix + "_" + str(idx) + "." + ext
        else: new_name = filepath + "/" + str(idx) + "." + ext
        os.system(f"mv {old_name} {new_name}")


if __name__    == "__main__":
    changeFileNames()
