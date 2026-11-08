import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
            absolute_path = os.path.abspath(working_directory)
            target_content = os.path.normpath(os.path.join(absolute_path, file_path))
        # Will be True or False
            valid_target_dir = os.path.commonpath([absolute_path, target_content]) == absolute_path
            if not valid_target_dir:
                result = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
                return result
            elif not os.path.isfile(target_content):
                 return f'Error: File not found or is not a regular file: "{file_path}"'
            else:
                with open(target_content, "r") as f:
                     file_content_string = f.read(MAX_CHARS)
                     if f.read(1):
                          file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            
    except Exception as e:
        return f"Error: {e}"