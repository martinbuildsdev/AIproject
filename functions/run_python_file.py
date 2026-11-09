import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_dir]
            if args:
                command.extend(args)
            result = subprocess.run(command,
                                    cwd=absolute_path,
                                    capture_output= True,
                                    text=True,
                                    timeout=30)
            output = ""
            if result.returncode != 0:
                output += f"Process exited with code {result.returncode}\n"
            if not result.stdout and not result.stderr:
                output += "No output produced"
            else:
            
                if result.stdout:
                    output += f"STDOUT: {result.stdout}\n"

                if result.stderr:
                    output += f"STDERR: {result.stderr}"
            return output

           
    except Exception as e:
        return f"Error: executing Python file: {e}"