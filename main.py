def clean_song_data(songs):
    cleaned = []
    for song in songs:
        cleaned.append({
            'title': song.get('title', ''),
            'view_count': song.get('view_count', '0'),
            'channel': song.get('channel', ''),
            'channel_follower_count': song.get('channel_follower_count', '0')
        })
    return cleaned
import csv

def read_youtube_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

if __name__ == "__main__":
    csv_path = "../youtube-top-100-songs-2025.csv"
    songs = read_youtube_csv(csv_path)
    print(f"Loaded {len(songs)} songs from CSV.")
    for song in songs[:5]:
        print(song)
    cleaned_songs = clean_song_data(songs)
    print(f"Loaded {len(cleaned_songs)} cleaned songs from CSV.")
    for song in cleaned_songs[:5]:
        print(song)


def get_top_songs_by_views(songs, n):
    # Reference at least 3 columns: title, view_count, channel
    sorted_songs = sorted(songs, key=lambda x: int(x['view_count']), reverse=True)
    return [{
        'title': song['title'],
        'view_count': int(song['view_count']),
        'channel': song['channel']
    } for song in sorted_songs[:n]]

# Test cases for get_top_songs_by_views
def test_get_top_songs_by_views():
    test_data = [
        {'title': 'Song A', 'view_count': '100', 'channel': 'Channel X'},
        {'title': 'Song B', 'view_count': '200', 'channel': 'Channel Y'},
        {'title': 'Song C', 'view_count': '50', 'channel': 'Channel Z'},
        {'title': 'Song D', 'view_count': '300', 'channel': 'Channel W'},
    ]
    # General case: get top 2
    result1 = get_top_songs_by_views(test_data, 2)
    assert result1[0]['title'] == 'Song D' and result1[1]['title'] == 'Song B', "General case failed"
    # General case: get top 3
    result2 = get_top_songs_by_views(test_data, 3)
    assert result2[2]['title'] == 'Song A', "General case failed"
    # Edge case: n larger than dataset
    result3 = get_top_songs_by_views(test_data, 10)
    assert len(result3) == 4, "Edge case failed"
    # Edge case: n = 0
    result4 = get_top_songs_by_views(test_data, 0)
    assert result4 == [], "Edge case failed"
    print("All tests for get_top_songs_by_views passed.")

def average_duration_by_category(songs, category):
    # Reference at least 3 columns: duration, categories, title
    filtered = [s for s in songs if category in s['categories']]
    if not filtered:
        return 0
    total_duration = sum(int(s['duration']) for s in filtered)
    avg = total_duration / len(filtered)
    return avg

# Test cases for average_duration_by_category
def test_average_duration_by_category():
    test_data = [
        {'title': 'Song A', 'duration': '100', 'categories': 'Pop'},
        {'title': 'Song B', 'duration': '200', 'categories': 'Pop;Rock'},
        {'title': 'Song C', 'duration': '50', 'categories': 'Rock'},
        {'title': 'Song D', 'duration': '300', 'categories': 'Pop'},
    ]
    # General case: Pop
    avg1 = average_duration_by_category(test_data, 'Pop')
    assert abs(avg1 - 200) < 1e-6, "General case failed"
    # General case: Rock
    avg2 = average_duration_by_category(test_data, 'Rock')
    assert abs(avg2 - 125) < 1e-6, "General case failed"
    # Edge case: category not present
    avg3 = average_duration_by_category(test_data, 'Jazz')
    assert avg3 == 0, "Edge case failed"
    # Edge case: only one song in category
    avg4 = average_duration_by_category(test_data, 'Pop;Rock')
    assert abs(avg4 - 200) < 1e-6, "Edge case failed"
    print("All tests for average_duration_by_category passed.")
