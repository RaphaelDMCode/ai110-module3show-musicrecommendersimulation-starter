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

    # --- User preference profiles ---

    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.90,
        "target_tempo_bpm": 128,
        "target_valence": 0.85,
        "target_danceability": 0.85,
        "target_acousticness": 0.10,
        "likes_acoustic": False,
    }

    chill_lofi = {
        "favorite_genre": "lo-fi",
        "favorite_mood": "calm",
        "target_energy": 0.30,
        "target_tempo_bpm": 75,
        "target_valence": 0.50,
        "target_danceability": 0.35,
        "target_acousticness": 0.75,
        "likes_acoustic": True,
    }

    deep_intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "angry",
        "target_energy": 0.95,
        "target_tempo_bpm": 150,
        "target_valence": 0.25,
        "target_danceability": 0.45,
        "target_acousticness": 0.05,
        "likes_acoustic": False,
    }

    # Select the active profile here
    profiles = {
        "High-Energy Pop": high_energy_pop,
        "Chill Lofi": chill_lofi,
        "Deep Intense Rock": deep_intense_rock,
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  TOP RECOMMENDATIONS — {profile_name}")
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
