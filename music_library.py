class Track:
    total_plays = 0

    def __init__(self, title: str, artist: str, duration: int) -> None:
        if not title.strip():
            raise ValueError("title must not be empty")
        if not artist.strip():
            raise ValueError("artist must not be empty")
        if duration <= 0:
            raise ValueError("duration must be greater than 0 seconds")

        self._title = title
        self._artist = artist
        self._duration = duration
        self.play_count = 0

    @property
    def title(self) -> str:
        return self._title

    @property
    def artist(self) -> str:
        return self._artist

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Duration must be positive")
        self._duration = value

    @property
    def duration_formatted(self) -> str:
        minutes, seconds = divmod(self._duration, 60)
        return f"{minutes}:{seconds:02d}"

    def play(self) -> None:
        Track.total_plays += 1
        self.play_count += 1
        print(f"Now playing: {self._title} by {self._artist}")

    def get_info(self) -> str:
        minutes, seconds = divmod(self._duration, 60)
        return (
            f"Title: {self._title} | Artist: {self._artist} | "
            f"Duration: {minutes}:{seconds:02d}"
        )

    def __str__(self) -> str:
        return (
            f"{self._title} by {self._artist} "
            f"({self.duration_formatted})"
        )

    def __repr__(self) -> str:
        return (
            f"Track({self._title!r}, {self._artist!r}, "
            f"{self._duration!r})"
        )

    def extend_duration(self, extra_seconds: int) -> None:
        self._duration += extra_seconds
        minutes, seconds = divmod(self._duration, 60)
        print(f"Duration extended. New total duration: {minutes}:{seconds:02d}")


class Song(Track):
    def __init__(
        self, title: str, artist: str, duration: int, genre: str
    ) -> None:
        super().__init__(title, artist, duration)
        self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    def get_info(self) -> str:
        return f"{super().get_info()} | Genre: {self._genre}"

    def __str__(self) -> str:
        return f"{super().__str__()} [Genre: {self._genre}]"

    def __repr__(self) -> str:
        return (
            f"Song({self._title!r}, {self._artist!r}, "
            f"{self._duration!r}, {self._genre!r})"
        )

    def play(self) -> None:
        Track.total_plays += 1
        self.play_count += 1
        print(
            f"Now playing {self._genre} song: "
            f"{self._title} by {self._artist}"
        )


class Episode(Track):
    def __init__(
        self,
        title: str,
        host: str,
        duration: int,
        episode_number: int,
    ) -> None:
        super().__init__(title, host, duration)
        self._host = host
        self._episode_number = episode_number

    @property
    def host(self) -> str:
        return self._host

    @property
    def episode_number(self) -> int:
        return self._episode_number

    def __str__(self) -> str:
        return (
            f"{self._title} - Episode {self._episode_number}, "
            f"hosted by {self._host} ({self.duration_formatted})"
        )

    def __repr__(self) -> str:
        return (
            f"Episode({self._title!r}, {self._host!r}, "
            f"{self._duration!r}, {self._episode_number!r})"
        )

    def play(self) -> None:
        Track.total_plays += 1
        self.play_count += 1
        print(
            f"Now playing podcast: {self._title} - Episode "
            f"{self._episode_number}, hosted by {self._host}"
        )


class Audiobook(Track):
    def __init__(
        self,
        title: str,
        narrator: str,
        duration: int,
        chapter_count: int,
    ) -> None:
        super().__init__(title, narrator, duration)
        self._narrator = narrator
        self._chapter_count = chapter_count
        self._current_chapter = 1

    @property
    def narrator(self) -> str:
        return self._narrator

    @property
    def chapter_count(self) -> int:
        return self._chapter_count

    @property
    def current_chapter(self) -> int:
        return self._current_chapter

    def __str__(self) -> str:
        return (
            f"{self._title}, narrated by {self._narrator} "
            f"({self.duration_formatted}; chapter "
            f"{self._current_chapter}/{self._chapter_count})"
        )

    def __repr__(self) -> str:
        return (
            f"Audiobook({self._title!r}, {self._narrator!r}, "
            f"{self._duration!r}, {self._chapter_count!r})"
        )

    def next_chapter(self) -> None:
        if self._current_chapter < self._chapter_count:
            self._current_chapter += 1

    def play(self) -> None:
        Track.total_plays += 1
        self.play_count += 1
        print(
            f"Now playing audiobook: {self._title} - "
            f"Chapter {self._current_chapter}, narrated by {self._narrator}"
        )


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self._list_tracks: list[Track] = []

    def add_track(self, track: Track) -> None:
        self._list_tracks.append(track)

    def get_total_duration(self) -> int:
        return sum(track.duration for track in self._list_tracks)

    @property
    def total_duration_formatted(self) -> str:
        total_seconds = self.get_total_duration()
        hours, remaining_seconds = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remaining_seconds, 60)
        return f"{hours}:{minutes:02d}:{seconds:02d}"

    def play_all(self) -> None:
        for track in self._list_tracks:
            track.play()


def run_demo() -> None:
    track = Track("Bohemian Rhapsody", "Queen", 354)
    song = Song("Imagine", "John Lennon", 183, "Rock")
    episode = Episode("Tech Talk", "Jane Smith", 1800, 42)
    audiobook = Audiobook("The Hobbit", "Martin Freeman", 39600, 19)

    print(f"Track properties: {track.title}, {track.artist}, {track.duration}")
    track.duration = 360
    print(f"Updated track duration: {track.duration_formatted}")
    print(track.get_info())
    track.extend_duration(10)

    print(f"Song genre: {song.genre}")
    print(song.get_info())
    print(f"Episode host and number: {episode.host}, {episode.episode_number}")
    print(
        f"Audiobook narrator and chapters: {audiobook.narrator}, "
        f"{audiobook.chapter_count}"
    )
    audiobook.next_chapter()
    print(f"Current audiobook chapter: {audiobook.current_chapter}")

    content_items: list[Track] = [track, song, episode, audiobook]
    print("Playing mixed content:")
    for content in content_items:
        content.play()

    print("Content representations:")
    for content in content_items:
        print(content)
        print(repr(content))

    playlist = Playlist("My Favorites")
    for content in content_items:
        playlist.add_track(content)
    print(f"Playlist: {playlist.name}")
    print(f"Total duration: {playlist.get_total_duration()} seconds")
    print(f"Formatted duration: {playlist.total_duration_formatted}")
    playlist.play_all()


def test_validation() -> None:
    validation_cases = (
        ("empty title", lambda: Track("", "Queen", 354)),
        ("empty artist", lambda: Track("Bohemian Rhapsody", "", 354)),
        ("zero duration", lambda: Track("Bohemian Rhapsody", "Queen", 0)),
    )

    for description, create_track in validation_cases:
        try:
            create_track()
        except ValueError:
            print(f"PASSED: {description}")
        else:
            print(f"FAILED: {description} did not raise ValueError")

    track = Track("Bohemian Rhapsody", "Queen", 354)
    try:
        track.duration = 0
    except ValueError:
        print("PASSED: invalid duration via property setter")
    else:
        print("FAILED: invalid duration via property setter did not raise ValueError")


if __name__ == "__main__":
    run_demo()
    test_validation()
