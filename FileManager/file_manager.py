import os
import shutil


def main():
    current_directory = os.path.abspath(os.path.dirname(__file__))
    print_prompt()

    while True:
        user_input = input("> ").strip()

        if user_input == 'quit':
            break
        elif user_input == 'pwd':
            print(current_directory)
        elif user_input == 'ls':
            list_directory_contents(current_directory)
        elif user_input.startswith('ls -l'):
            list_directory_contents_with_size(current_directory, human_readable=False)
        elif user_input.startswith('ls -lh'):
            list_directory_contents_with_size(current_directory, human_readable=True)
        elif user_input.startswith('rm'):
            remove_files_by_extension(user_input, current_directory)
        elif user_input.startswith('mv'):
            move_files_by_extension(user_input, current_directory)
        elif user_input.startswith('cp'):
            copy_files_by_extension(user_input, current_directory)
        elif user_input.startswith('mkdir'):
            create_directory(user_input, current_directory)
        elif user_input == 'cd ..':
            current_directory = move_up(current_directory)
        elif user_input.startswith('cd '):
            current_directory = move_to_directory(user_input, current_directory)
        else:
            print("Invalid command")


def print_prompt():
    print("Input the command")


def move_up(current_directory):
    new_directory = os.path.dirname(current_directory)
    current_folder = os.path.basename(new_directory)
    print(current_folder)
    return new_directory


def move_to_directory(user_input, current_directory):
    _, path = user_input.split(' ', 1)
    new_directory = os.path.join(current_directory, path)

    if os.path.exists(new_directory) and os.path.isdir(new_directory):
        current_folder = os.path.basename(new_directory)
        print(current_folder)
        return new_directory
    else:
        print("Invalid command")
        return current_directory


def list_directory_contents(directory):
    items = os.listdir(directory)

    if not items:
        return

    subdirectories = [item for item in items if os.path.isdir(os.path.join(directory, item))]
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]

    print(*subdirectories, sep='\n')
    print(*files, sep='\n')


def list_directory_contents_with_size(directory, human_readable=False):
    items = os.listdir(directory)

    if not items:
        return

    subdirectories = [item for item in items if os.path.isdir(os.path.join(directory, item))]
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]

    for item in subdirectories:
        print(item)

    for file in files:
        size = os.stat(os.path.join(directory, file)).st_size

        if human_readable:
            print(f"{file} {humanize.naturalsize(size)}")
        else:
            print(f"{file} {size}")


def remove_files_by_extension(user_input, current_directory):
    _, *args = user_input.split()

    if not args:
        print("Specify the file extension")
        return

    extension = args[0]
    files_to_remove = [file for file in os.listdir(current_directory) if file.endswith(extension)]

    if not files_to_remove:
        print(f"File extension {extension} not found in this directory")
    else:
        for file in files_to_remove:
            os.remove(os.path.join(current_directory, file))


def create_directory(user_input, current_directory):
    _, *args = user_input.split()

    if not args:
        print("Specify the name of the directory to be made")
        return

    new_directory_name = args[0]
    new_directory_path = os.path.join(current_directory, new_directory_name)

    if os.path.exists(new_directory_path) and os.path.isdir(new_directory_path):
        print("The directory already exists")
    else:
        os.makedirs(new_directory_path)


def copy_files_by_extension(user_input, current_directory):
    _, *args = user_input.split()

    if len(args) != 2:
        print("Specify the file extension and the destination directory")
        return

    extension, destination_directory = args
    files_to_copy = [file for file in os.listdir(current_directory) if file.endswith(extension)]

    if not files_to_copy:
        print(f"File extension {extension} not found in this directory")
    else:
        for file in files_to_copy:
            source_path = os.path.join(current_directory, file)
            destination_path = os.path.join(destination_directory, file)

            if os.path.exists(destination_path):
                replace_file = input(f"{file} already exists in this directory. Replace? (y/n): ")

                if replace_file.lower() == 'y':
                    shutil.copy(source_path, destination_path)
            else:
                shutil.copy(source_path, destination_path)


def move_files_by_extension(user_input, current_directory):
    _, *args = user_input.split()

    if len(args) != 2:
        print("Specify the file extension and the destination directory")
        return

    extension, destination_directory = args
    files_to_move = [file for file in os.listdir(current_directory) if file.endswith(extension)]

    if not files_to_move:
        print(f"File extension {extension} not found in this directory")
    else:
        for file in files_to_move:
            source_path = os.path.join(current_directory, file)
            destination_path = os.path.join(destination_directory, file)

            if os.path.exists(destination_path):
                replace_file = input(f"{file} already exists in this directory. Replace? (y/n): ")

                if replace_file.lower() == 'y':
                    shutil.move(source_path, destination_path)
            else:
                shutil.move(source_path, destination_path)


if __name__ == "__main__":
    main()
