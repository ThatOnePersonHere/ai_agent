import os

def get_files_info(working_directory, directory=None):
    try:
        target_path = os.path.abspath(os.path.join(working_directory,directory or ""))
        abs_working_dir = os.path.abspath(working_directory)

        #if directory is outside of working directory, error mssg
        if not target_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        items_found = []
        for item in os.listdir(target_path):
            item_path = os.path.join(target_path, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            items_found = 
        return items_found
    except Exception as e:
        return f"Error: {str(e)}"