import os
import subprocess
import shutil

#input = input("Bitte Order Namen eingeben:")
#print(input)
output_folder_path = ".\\output"

if os.path.exists(output_folder_path) and os.path.isdir(output_folder_path):
    print(f"The folder at {output_folder_path} exists.")
    shutil.rmtree(output_folder_path)
    print(f"The folder at {output_folder_path} and its contents have been deleted.")
else:
    print(f"The folder at {output_folder_path} does not exist.")

os.mkdir(output_folder_path)
print("Der Ordner wurde erstellt")


# Define the PowerShell script you want to execute
powershell_script = r"""
ffmpeg -i .\\input\\video.mp4 -r 10.7 -q:v 2 .\{}\%d.jpg
""".format(output_folder_path)

# Use subprocess to run the PowerShell script
completed_process = subprocess.run(["powershell", "-command", powershell_script], text=True, capture_output=True)

# Check if the PowerShell script executed successfully
if completed_process.returncode == 0:
    print("PowerShell script executed successfully")
    print("PowerShell output:")
    print(completed_process.stdout)
else:
    print("PowerShell script encountered an error")
    print("PowerShell error output:")
    print(completed_process.stderr)