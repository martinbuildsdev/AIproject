import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
    # Will be True or False
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        if not valid_target_dir:
            result = f"Result for '{directory}' directory:"
            return f'{result}\n Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            if directory == ".":
                directory = "current"
            result = f"Result for '{directory}' directory:"
            names = os.listdir(target_dir)
            results = []
            for name in names:
                results.append(f"  - {name}: file_size={os.path.getsize(os.path.join(target_dir, name))}, is_dir={os.path.isdir(os.path.join(target_dir, name))}")

             
            return f"{result}\n" + "\n".join(results)
        
        if os.path.isdir(target_dir):
            return f'Success: "{directory}" is within the working directory'
        else:
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f"Error: {e}"