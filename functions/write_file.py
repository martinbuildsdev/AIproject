import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
                absolute_path = os.path.abspath(working_directory)
                target_content = os.path.normpath(os.path.join(absolute_path, file_path))
            # Will be True or False
                valid_target_dir = os.path.commonpath([absolute_path, target_content]) == absolute_path
                if not valid_target_dir:
                    result = f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
                    return result
                elif  os.path.isdir(target_content):
                     return f'Error: Cannot write to "{file_path}" as it is a directory'
                else: 
                    os.makedirs(os.path.dirname(target_content), exist_ok=True)
                    with open(target_content, "w") as f:
                         f.write(content)
                    
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
                
    except Exception as e:
        return f"Error: {e}"