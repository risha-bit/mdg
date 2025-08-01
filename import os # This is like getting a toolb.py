import os  # This is like getting a toolbox to work with files and folders

def list_files_with_extension(directory, extension):

# Think of this function like a detective that finds specific types of files!    
    # STEP 1: Make sure the file type has a dot in front
    # Like changing "txt" to ".txt"
    if not extension.startswith("."):
        extension = "." + extension
    
    
    try:  
        # STEP 2: Look inside the folder and get a list of everything
        files = os.listdir(directory)
        # This is like opening a drawer and seeing: ['photo.jpg', 'letter.txt', 'song.mp3']
        
        # STEP 3: Pick out only the files that end with our extension
        matching_files = [file for file in files if file.endswith(extension)]
        # This is like saying "give me only the things that end with .txt"
        # So from ['photo.jpg', 'letter.txt', 'song.mp3'] we'd get ['letter.txt']
        
        # STEP 4: Tell the user what we found
        if matching_files:  # If we found some files
            print(f"Files with extension '{extension}' in '{directory}':")
            for file in matching_files:  # Show each one
                print(file)
        else:  # If we found nothing
            print(f"No files with extension '{extension}' found in '{directory}'.")
    
    # STEP 5: Handle problems gracefully
    except FileNotFoundError:  # If the folder doesn't exist
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:  # If any other weird thing happens
        print(f"An error occurred: {e}")

# STEP 6: Actually run the program
directory = input("Enter the directory path: ")  # Ask user: "Where should I look?"
extension = input("Enter the file extension (e.g., txt): ")  # Ask: "What type of files?"
list_files_with_extension(directory, extension)  # Go find those files!