import json
future_silja = {}
future_silja["first_name"] = "Silja"
future_silja["last name"] = "Xane"
future_silja["Job"] = [{"field": "Technology",
                        "purpose": "Solve problems",
                        "Role": "Leader and Coach"}]
future_silja["has_potential"] = True
future_silja["Money in pocket"] = 150

with open("future_silja.json", "w") as file_object:
    json.dump(future_silja, file_object)

# For second file-open, where you want to open your file (as seen above), do the following:

import json
with open("future_silja.json") as file_object:
    future_silja = json.load(file_object)

    
for k, v in future_silja.items():
    print(k, ':', v)







# TASK 1
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. 
# Then write another script that opens myfile.txt, and reads and prints its contents. 
# Run your two scripts from the system command line. 

# Does the new file show up in the directory where you ran your scripts? 

# What if you add a different directory path to the filename passed to open?

# Note: file write methods do not add newline characters to your strings; 
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.



