import os

filepath_list = ["/Users/amitabhishek/Desktop/workingDir/Python/destination/compressed.zip"]
filepath = filepath_list[0]
# Get the base name of the file
basename = os.path.basename(filepath)

print(basename)