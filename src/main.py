"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile — target values used for scoring each song
    user_prefs = {
        # Categorical preferences (must match values used in songs.csv)
        "favorite_genre": "pop",
        "favorite_mood": "happy",

        # Numeric targets (0.0 – 1.0 scale unless noted)
        "target_energy": 0.80,        # high energy, upbeat tracks
        "target_tempo_bpm": 120,      # fast, danceable tempo
        "target_valence": 0.85,       # very positive, feel-good
        "target_danceability": 0.80,  # strong groove
        "target_acousticness": 0.20,  # prefers produced/electronic texture

        # Boolean flag — drives a hard boost or filter in scoring
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  TOP RECOMMENDATIONS")
    print("=" * 50)

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  —  {song['artist']}")
        print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}")
        print(f"    Score: {score:.2f}")
        print("    Why:")
        for reason in reasons:
            print(f"      • {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
