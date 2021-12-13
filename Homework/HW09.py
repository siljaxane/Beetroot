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