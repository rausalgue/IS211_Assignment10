/*music artists, the albums they create and the songs that appear on those albums*/
/*name of the song, the associated album this song appears on, the track number of the song, and how long
the song is (in seconds)*/

CREATE DATABASE development;

CREATE TABLE Artists (
  Identifier INTEGER PRIMARY KEY,
  Name TEXT
);

CREATE TABLE Albums (
    Identifier INTEGER PRIMARY KEY,
    Name TEXT,
    Artist INTEGER,
    FOREIGN KEY (Artist) REFERENCES Artists(Identifier)
);

CREATE TABLE Songs (
    Identifier INTEGER PRIMARY KEY,
    Name TEXT,
    TrackNumber INTEGER,
    TrackDuration INTEGER,
    Album INTEGER,
    Artist INTEGER,
    FOREIGN KEY (Album) REFERENCES Albums(Identifier),
    FOREIGN KEY (Artist) REFERENCES Artists(Identifier)
);
