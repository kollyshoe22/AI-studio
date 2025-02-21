import os  # Import the os module for interacting with the filesystem

def run_model_on_file(file_path):
    """
    Placeholder function for processing a file with a model.
    Replace this with actual model logic (e.g., ML inference, data processing, etc.).
    
    Args:
        file_path (str): The full path of the file to be processed.
    """
    print(f"Processing: {file_path}")
    # TODO: Add model inference logic here, such as:
    # - Loading the file
    # - Running it through a machine learning model
    # - Saving or outputting results

def process_folder(folder_path):
    """
    Iterates through all files in the given folder and processes each one.

    Args:
        folder_path (str): The path to the folder containing files to process.
    """
    if not os.path.isdir(folder_path):  # Check if the provided path is a valid directory
        print("Invalid folder path. Please provide a valid directory.")
        return  # Exit the function if the path is invalid
    
    # Loop through all items (files and subdirectories) in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)  # Construct the full file path
        
        if os.path.isfile(file_path):  # Ensure it's a file, not a subdirectory
            run_model_on_file(file_path)  # Call the model-processing function on the file

if __name__ == "__main__":
    # Prompt the user to input the folder path
    folder_path = input("Enter the path to the folder: ").strip()  # Strip removes any extra spaces
    process_folder(folder_path)  # Call the function to start processing files
