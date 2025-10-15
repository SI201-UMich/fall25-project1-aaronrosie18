# Project 1 main code file


import csv

def read_youtube_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        return rows

if __name__ == "__main__":
    csv_path = "../youtube-top-100-songs-2025.csv"
    songs = read_youtube_csv(csv_path)
    print(f"Loaded {len(songs)} songs from CSV.")
    for song in songs[:5]:
        print(song)
