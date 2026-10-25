# Music Library Manager

A small Python project demonstrating object-oriented programming through a
music and audio-content library. It models tracks and specialized content,
uses encapsulation and properties to manage state, and supports polymorphic
playback and playlists.

## Project contents

All implementation is in [`music_library.py`](./music_library.py).

- **`Track`** is the base class. It stores a title, artist, and duration in
  seconds; validates these values at construction; and exposes them through
  properties. The duration property can be updated only to a positive value.
  Tracks can be played, have their duration extended, return formatted
  information, and display readable `str` and constructor-style `repr`
  representations. `Track.total_plays` counts plays across all content, while
  each instance has its own `play_count`.
- **`Song`** extends `Track` with a genre, genre-aware playback, and genre
  details in its information and display representations.
- **`Episode`** extends `Track` with a podcast host and episode number, and
  provides podcast-specific playback and display output.
- **`Audiobook`** extends `Track` with a narrator, chapter count, and a current
  chapter that starts at 1. `next_chapter()` advances the current chapter
  without going beyond the last chapter.
- **`Playlist`** stores a name and a collection of tracks. It can add content,
  calculate total duration in seconds, return that duration in `H:MM:SS`
  format, and play all items. Since the content classes share the `Track`
  interface, a playlist can contain mixed content types.
- **`run_demo()`** demonstrates the classes, properties, specialized behavior,
  polymorphic playback, string representations, and playlist use.
- **`test_validation()`** checks invalid track construction and duration
  assignment, printing `PASSED` or `FAILED` for each case.

## Requirements

- Python 3.9 or later (uses built-in generic type annotations such as
  `list[Track]`)
- No third-party packages

## Run the demo and validation checks

From the project directory, run:

```powershell
python music_library.py
```

This runs `run_demo()` followed by `test_validation()`. To run either function
after importing the module:

```python
from music_library import run_demo, test_validation

run_demo()
test_validation()
```

Importing `music_library` does not automatically run the demo.

## Basic usage

```python
from music_library import Audiobook, Episode, Playlist, Song, Track

playlist = Playlist("My Favorites")
playlist.add_track(Song("Imagine", "John Lennon", 183, "Rock"))
playlist.add_track(Episode("Tech Talk", "Jane Smith", 1800, 42))
playlist.add_track(
    Audiobook("The Hobbit", "Martin Freeman", 39600, 19)
)

print(playlist.total_duration_formatted)
playlist.play_all()
```
