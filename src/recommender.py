from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a numeric score and list of reasons for how well a song matches user preferences."""
    score = 0.0
    reasons: List[str] = []

    # --- Categorical matches ---
    if song["genre"] == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append(f"genre match (+2.0)")

    if song["mood"] == user_prefs.get("favorite_mood"):
        score += 1.5
        reasons.append(f"mood match (+1.5)")

    # --- Numeric feature closeness (0-1 scale features) ---
    numeric_features = [
        ("energy",        "target_energy",        1.0),
        ("valence",       "target_valence",        1.0),
        ("danceability",  "target_danceability",   1.0),
        ("acousticness",  "target_acousticness",   1.0),
    ]
    for feature, pref_key, weight in numeric_features:
        if pref_key in user_prefs:
            closeness = 1.0 - abs(user_prefs[pref_key] - song[feature])
            points = round(weight * closeness, 2)
            score += points
            reasons.append(f"{feature} closeness (+{points})")

    # --- Tempo closeness (normalized over ±60 bpm window) ---
    if "target_tempo_bpm" in user_prefs:
        diff = abs(user_prefs["target_tempo_bpm"] - song["tempo_bpm"])
        closeness = max(0.0, 1.0 - diff / 60.0)
        points = round(0.5 * closeness, 2)
        score += points
        reasons.append(f"tempo closeness (+{points})")

    # --- Acoustic bonus ---
    if user_prefs.get("likes_acoustic") and song["acousticness"] >= 0.6:
        score += 1.0
        reasons.append("acoustic bonus (+1.0)")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in the catalog and return the top k sorted by score descending."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [(song, score, reasons) for song, score, reasons in scored[:k]]
