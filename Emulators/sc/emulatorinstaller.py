import os
import shutil
import re

def check_path(check_plugin):
    # Define the specific paths to check on the drive
    check_plugin_path = "wiiflow\\plugins_data\\platform.ini"  # First path
    plugin_type_path = "wiiflow\\source_menu\\source_menu.ini"  # Second path, change as needed
    
    # Format the full paths
    full_path_1 = os.path.join(check_plugin + ":", check_plugin_path)
    full_path_2 = os.path.join(check_plugin + ":", plugin_type_path)
    
    # Check if the first path exists
    if os.path.exists(full_path_1):
        print("Plugins found")
        
        # Now check the second path
        if os.path.exists(full_path_2):
            print("Source Menu found")
            
            # Loop until a valid choice is made
            while True:
                print("What source menu are you using?")
                print("1. Rhapsodii Shima/Rhapsodii")
                print("2. Wiiflow 4 Masterpiece Mod")
                print("3. Other")
                
                try:
                    plugin_type = int(input("Enter the number corresponding to your choice: "))
                    
                    if plugin_type in [1, 2, 3]:  # Valid selections
                        return plugin_type  # Return the valid plugin type
                    else:
                        print("Invalid selection. Please choose 1, 2, or 3.")
                
                except ValueError:
                    print("Invalid input. Please enter a number (1, 2, or 3).")
        else:
            print("Source Menu not found.")
            return None  # Return None to indicate failure
    else:
        print("Plugins not found. Please install plugins pack.")
        return None  # Return None to indicate failure

def copy_files(source_folder, destination_drive):
    # Define the destination path as the root of the drive
    destination_path = os.path.join(destination_drive + ":\\")
    
    try:
        # Check if the source folder exists
        if os.path.exists(source_folder):
            print(f"Copying files from {source_folder} to {destination_path}...")
            # Check if destination directory exists; if not, create it
            os.makedirs(destination_path, exist_ok=True)
            
            # Use shutil.copytree to copy files to the root of the drive
            # Set dirs_exist_ok=True to merge directories if they exist
            shutil.copytree(source_folder, os.path.join(destination_path, os.path.basename(source_folder)), dirs_exist_ok=True)
            print("Files copied successfully!")
        else:
            print("The specified source folder does not exist.")
    except Exception as e:
        print(f"An error occurred while copying files: {e}")

def clean_handhelds_file(check_plugin):
    # Path to the handhelds.ini file
    handhelds_path = os.path.join(check_plugin + ":", "wiiflow\\source_menu\\handhelds.ini")
    
    # Check if the handhelds.ini file exists
    if os.path.exists(handhelds_path):
        print(f"Opening {handhelds_path} to clean out the 'magic' section...")
        
        with open(handhelds_path, 'r') as file:
            lines = file.readlines()
        
        # Open the file for writing
        with open(handhelds_path, 'w') as file:
            skip = False
            for line in lines:
                # Check if we hit the magic line
                if line.strip() == "magic=4445534D":
                    skip = True  # Start skipping lines
                elif skip:
                    if line.startswith("["):  # Found a new section header, stop skipping
                        skip = False  # Stop skipping when reaching a new section
                        file.write(line)  # Write the new section header
                    elif "source=plugin" in line or line.startswith("magic=") or re.match(r'\[BUTTON_\d+\]', line):
                        # Skip these lines related to the magic section
                        continue
                else:
                    # If we are not skipping, write the line
                    file.write(line)
        print("Removed the magic section and its associated lines from the file.")
    else:
        print("handhelds.ini file not found.")

def get_highest_button_number(handhelds_path):
    buttons = 0  # Initialize buttons variable

    # Check if the handhelds.ini file exists
    if os.path.exists(handhelds_path):
        print(f"Opening {handhelds_path} to check button instances...")
        
        with open(handhelds_path, 'r') as file:
            content = file.read()
            
            # Use regex to find all instances of [BUTTON_(number)]
            button_matches = re.findall(r'\[BUTTON_(\d+)\]', content)
            
            # If matches found, convert to integers and find the maximum
            if button_matches:
                buttons = max(map(int, button_matches))
                print(f"The highest button number found is: {buttons}")
            else:
                print("No button instances found.")
    
    return buttons

def add_button_to_computers_file(check_plugin, new_button):
    # Path to the computers.ini file
    computers_path = os.path.join(check_plugin + ":", "wiiflow\\source_menu\\computers.ini")
    
    # Add the new button entry to the bottom of the file
    with open(computers_path, 'a') as file:  # Open in append mode
            file.write(f"\n[BUTTON_{new_button_handhelds}]\n")
            file.write(f"autoboot=\n")
            file.write(f"cat_page=1\n")
            file.write(f"category=0\n")
            file.write(f"hidden=no\n")
            file.write(f"pc98neko.png\n")
            file.write(f"image_s=pc98neko.png\n")
            file.write(f"magic=6E656B6F,6E656B7F\n")
            file.write(f"source=plugin\n")
            file.write(f"title=PC-9800\n") 
        
    print(f"PC98 Emualator was installed to computers.ini.")

# Main loop to repeatedly ask for the drive letter if there are any issues
while True:
    check_plugin = input("Enter the drive letter (e.g., C, D): ").upper()
    
    # Validate the drive letter
    if len(check_plugin) == 1 and check_plugin.isalpha():
        # Call the function to check the paths and get the plugin type
        plugin_type = check_path(check_plugin)
        
        if plugin_type == 1:  # Only ask for the source folder if plugin_type is 1
            source_folder = input("Enter the path of the folder you want to copy: ")
            copy_files(source_folder, check_plugin)  # Copy files to the root of the specified drive
            
            # Clean the handhelds.ini file before checking button numbers
            handhelds_path = os.path.join(check_plugin + ":", "wiiflow\\source_menu\\handhelds.ini")
            clean_handhelds_file(check_plugin)
            
            # After cleaning, check for the highest button number
            highest_buttons = get_highest_button_number(handhelds_path)
            
            # Add the new button to handhelds.ini
            new_button_handhelds = highest_buttons + 1
            with open(handhelds_path, 'a') as file:  # Open in append mode
                file.write(f"\n[BUTTON_{new_button_handhelds}]\n")
                file.write(f"autoboot=\n")
                file.write(f"cat_page=1\n")
                file.write(f"category=0\n")
                file.write(f"hidden=no\n")
                file.write(f"image=nintendo_ds.png\n")
                file.write(f"image_s=nintendo_ds.png\n")
                file.write(f"magic=4445534D\n")
                file.write(f"source=plugin\n")
                file.write(f"title=Nintendo DS\n")   
            print(f"DS Emulator Installed in handhelds.ini.")
            
            # Now add a new button to computers.ini
            new_button_computers = highest_buttons + 1  # Use the same number for simplicity
            add_button_to_computers_file(check_plugin, new_button_computers)
            
            break  # Exit loop after processing
        elif plugin_type in [2, 3]:
            print("No files will be copied for this selection.")
            break  # Exit loop for other valid selections
        else:
            print("Error: Could not find the necessary files. Please try again.")
    else:
        print("Invalid drive letter. Please enter a single letter (e.g., C, D).")
