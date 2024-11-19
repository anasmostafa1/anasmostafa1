import customtkinter as ctk
import minecraft_launcher_lib
import subprocess
import threading
import time

# Configuration
gamedir = "./.pycrack"
options = minecraft_launcher_lib.utils.generate_test_options()
options["gameDir"] = "./.pycrackdir"

# Generate Minecraft version list with major, minor, and patch versions
def generate_all_versions():
    versions = []
    max_major_version = 1
    max_minor_version = 21
    patch_versions = {
        10: 5,
        11: 5,
        12: 5,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 5,
        18: 5,
        19: 5,
        20: 5,
        21: 3, 
    }
    for major in range(1, max_major_version + 1):  # Major versions (only 1.x for now)
        for minor in range(1, max_minor_version + 1):  # Minor versions (e.g., 1.1 to 1.21)
            versions.append(f"{major}.{minor}")  # Add base version (e.g., 1.16)
            max_patches = patch_versions.get(minor, 0)
            for patch in range(1, max_patches + 1):  # Add patch versions (e.g., 1.16.1, 1.16.2)
                versions.append(f"{major}.{minor}.{patch}")
    return versions.reverse()

minecraft_versions = generate_all_versions()

# Function to simulate installation progress
def simulate_progress(progress_bar, progress_label):
    for value in range(0, 101, 5):
        time.sleep(0.1)  # Simulates a step in progress
        progress_bar.set(value / 100)
        progress_label.configure(text=f"Progress: {value}%")
    progress_label.configure(text="Installation Complete")

# Function to install and launch Minecraft
def install_and_launch():
    user = username_entry.get().strip()
    version = version_combobox.get().strip()
    
    if not user or not version or version == "Select Version":
        ctk.CTkMessagebox(title="Input Error", message="Both username and version must be provided!")
        return
    
    options["username"] = user
    progress_label.configure(text="Starting installation...")
    progress_bar.set(0)

    # Run installation and progress in a separate thread
    def run_installation():
        try:
            simulate_progress(progress_bar, progress_label)  # Replace with actual progress tracking if supported
            minecraft_launcher_lib.install.install_minecraft_version(version, gamedir)
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, gamedir, options)
            subprocess.call(minecraft_command)
            ctk.CTkMessagebox(title="Success", message=f"Version {version} installed and launched successfully!")
        except Exception as e:
            ctk.CTkMessagebox(title="Error", message=f"An error occurred: {e}")
        finally:
            progress_label.configure(text="")

    threading.Thread(target=run_installation).start()

# Initialize `customtkinter`
ctk.set_appearance_mode("System")  # Options: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue" (default), "green", "dark-blue"

# Create GUI window
root = ctk.CTk()
root.title("Minecraft Launcher")
root.geometry("400x300")

# Username Label and Entry
username_label = ctk.CTkLabel(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
username_entry = ctk.CTkEntry(root, width=250, placeholder_text="Enter your username")
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Version Label and Combo Box
version_label = ctk.CTkLabel(root, text="Minecraft Version:")
version_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
version_combobox = ctk.CTkComboBox(root, values=minecraft_versions)
version_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")
version_combobox.set("Select Version")  # Default text

# Progress Bar and Label
progress_label = ctk.CTkLabel(root, text="")
progress_label.grid(row=2, column=0, columnspan=2, pady=5)
progress_bar = ctk.CTkProgressBar(root, width=300)
progress_bar.grid(row=3, column=0, columnspan=2, pady=10)
progress_bar.set(0)

# Launch Button
launch_button = ctk.CTkButton(root, text="Install & Launch", command=install_and_launch)
launch_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start GUI event loop
root.mainloop()
