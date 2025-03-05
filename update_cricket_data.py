import os
import json
import pandas as pd


os.system("wget -O matches.zip https://cricsheet.org/downloads/all_json.zip")
os.system("unzip -o matches.zip -d cricsheet_data")

print(" Cricsheet data downloaded and extracted!")


folder_path = "cricsheet_data/"

def process_match(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    match_info = {
        "format": data["info"]["match_type"],  # T20, ODI, Test
        "team1": data["info"]["teams"][0],
        "team2": data["info"]["teams"][1],
        "toss_winner": data["info"]["toss"]["winner"],
        "match_winner": data["info"]["outcome"].get("winner", "No Result"),
        "venue": data["info"]["venue"],
        "date": data["info"]["dates"][0]
    }
    return match_info


matches = []
for file in os.listdir(folder_path):
    if file.endswith(".json"):
        match_data = process_match(os.path.join(folder_path, file))
        matches.append(match_data)


df = pd.DataFrame(matches)
df.to_csv("updated_cricket_matches.csv", index=False)

print(" Updated dataset saved as updated_cricket_matches.csv!")
