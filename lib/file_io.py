import os

def write_file(file_name, file_content):
    """
    Creates a new .txt file or overwrites an existing file with the given content.
    
    :param file_name: Name of the file without extension.
    :param file_content: Content to write in the file.
    """
    full_path = f"{file_name}.txt"
    with open(full_path, "w") as file:
            file.write(file_content)
    pass

def append_file(file_name, append_content):
    """
    Appends content to an existing .txt file.
    
    :param file_name: Name of the file without extension.
    :param append_content: Content to append to the file.
    """
    full_path = os.path.join(str(file_name) + ".txt") if isinstance(file_name, str) else str(file_name) + ".txt"
    
    with open(full_path, "a") as file:
        if os.path.getsize(full_path) > 0 and not append_content.startswith("\n"):
            file.write("\n") 
        file.write(append_content) 
    pass

def read_file(file_name):
    """
    Reads and returns the content of a .txt file.
    
    :param file_name: Name of the file without extension.
    :return: Content of the file as a string.
    """
    full_path = os.path.join(str(file_name) + ".txt") if isinstance(file_name, str) else str(file_name) + ".txt"
    
    if not os.path.exists(full_path):
        return "File not found."

    with open(full_path, "r") as file:
        return file.read().strip() 
    pass
