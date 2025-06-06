import sqlite3

# Connect (or create) a SQLite database file
conn = sqlite3.connect('rock_albums.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rank INTEGER,
    artist TEXT,
    album TEXT,
    year INTEGER,
    genre TEXT,
    notes TEXT
);
''')
# THE DATA COMES FROM 50 best rock albums from LOUDER SOUND
# Insert data
albums = [
    (1, 'The Clash', 'London Calling', 1979, 'Punk Rock', 'Politically charged and innovative.'),
    (2, 'Metallica', 'Ride the Lightning', 1984, 'Heavy Metal', 'A landmark thrash metal album.'),
    (3, 'AC/DC', 'Let There Be Rock', 1977, 'Hard Rock', 'High-energy and riff-heavy.'),
    (4, 'Radiohead', 'OK Computer', 1997, 'Alternative Rock', 'Critically acclaimed and influential.'),
    (5, 'The Rolling Stones', 'Exile on Main St.', 1972, 'Classic Rock', 'A rootsy and raw masterpiece.'),
    (6, 'Led Zeppelin', 'Led Zeppelin IV', 1971, 'Classic Rock', 'Includes "Stairway to Heaven".'),
    (7, 'Pink Floyd', 'The Dark Side of the Moon', 1973, 'Progressive Rock', 'Concept album with groundbreaking production.'),
    (8, 'The Beatles', 'Abbey Road', 1969, 'Rock', 'Famous for its medley on side two.'),
    (9, 'Nirvana', 'Nevermind', 1991, 'Grunge', 'Brought grunge to the mainstream.'),
    (10, 'Black Sabbath', 'Paranoid', 1970, 'Heavy Metal', 'Defined early heavy metal.'),
    (11, 'The Jimi Hendrix Experience', 'Are You Experienced', 1967, 'Psychedelic Rock', 'Groundbreaking guitar work.'),
    (12, 'The Velvet Underground', 'The Velvet Underground & Nico', 1967, 'Art Rock', 'Dark and influential debut.'),
    (13, 'David Bowie', 'The Rise and Fall of Ziggy Stardust and the Spiders from Mars', 1972, 'Glam Rock', 'Concept album about a rock star.'),
    (14, 'Queen', 'A Night at the Opera', 1975, 'Rock', 'Includes "Bohemian Rhapsody".'),
    (15, 'The Who', "Who's Next", 1971, 'Rock', 'Includes classics like "Baba O\'Riley".'),
    (16, 'The Doors', 'The Doors', 1967, 'Psychedelic Rock', 'Debut album with iconic songs.'),
    (17, 'Fleetwood Mac', 'Rumours', 1977, 'Rock', 'Massive commercial and critical success.'),
    (18, 'Bruce Springsteen', 'Born to Run', 1975, 'Rock', 'Epic and cinematic.'),
    (19, 'U2', 'The Joshua Tree', 1987, 'Rock', 'Defined 80s rock anthems.'),
    (20, 'Elvis Presley', 'Elvis Presley', 1956, 'Rock and Roll', 'Debut album that launched a legend.'),
    (21, 'The Rolling Stones', 'Let It Bleed', 1969, 'Classic Rock', 'Includes "Gimme Shelter".'),
    (22, 'Bob Dylan', 'Highway 61 Revisited', 1965, 'Folk Rock', 'Includes "Like a Rolling Stone".'),
    (23, 'The Beach Boys', 'Pet Sounds', 1966, 'Pop Rock', 'Influential and complex arrangements.'),
    (24, 'Metallica', 'Master of Puppets', 1986, 'Heavy Metal', 'Thrash metal masterpiece.'),
    (25, 'Janis Joplin', 'Pearl', 1971, 'Blues Rock', 'Her final studio album.'),
    (26, 'AC/DC', 'Back in Black', 1980, 'Hard Rock', 'One of the best-selling albums ever.'),
    (27, 'The Ramones', 'Ramones', 1976, 'Punk Rock', 'Pioneering punk debut.'),
    (28, 'The Stooges', 'Raw Power', 1973, 'Proto-Punk', 'Raw and intense sound.'),
    (29, 'Led Zeppelin', 'Physical Graffiti', 1975, 'Classic Rock', 'Double album with diverse styles.'),
    (30, 'Talking Heads', 'Remain in Light', 1980, 'New Wave', 'Funky and experimental.'),
    (31, 'Pearl Jam', 'Ten', 1991, 'Grunge', 'Debut album that defined 90s rock.'),
    (32, 'The Smiths', 'The Queen Is Dead', 1986, 'Alternative Rock', 'Iconic indie rock album.'),
    (33, 'Soundgarden', 'Superunknown', 1994, 'Grunge', 'Dark and powerful.'),
    (34, 'Radiohead', 'Kid A', 2000, 'Alternative Rock', 'Experimental and electronic.'),
    (35, 'Oasis', "(What's the Story) Morning Glory?", 1995, 'Britpop', 'Britpop anthem album.'),
    (36, 'Foo Fighters', 'The Colour and the Shape', 1997, 'Alternative Rock', 'Includes "Everlong".'),
    (37, 'Green Day', 'Dookie', 1994, 'Punk Rock', 'Broke punk into the mainstream.'),
    (38, 'The White Stripes', 'Elephant', 2003, 'Garage Rock', 'Raw and bluesy.'),
    (39, 'The Killers', 'Hot Fuss', 2004, 'Alternative Rock', 'Debut with hit singles.'),
    (40, 'Kings of Leon', 'Only by the Night', 2008, 'Alternative Rock', 'Includes "Sex on Fire".'),
    (41, 'Arctic Monkeys', "Whatever People Say I Am, That's What I'm Not", 2006, 'Indie Rock', 'Critically acclaimed debut.'),
    (42, 'Muse', 'Black Holes and Revelations', 2006, 'Alternative Rock', 'Epic and cinematic.'),
    (43, 'The Black Keys', 'Brothers', 2010, 'Blues Rock', 'Raw and soulful.'),
    (44, 'Jack White', 'Blunderbuss', 2012, 'Rock', 'Debut solo album.'),
    (45, 'Queens of the Stone Age', 'Songs for the Deaf', 2002, 'Alternative Rock', 'Desert rock at its best.'),
    (46, 'The Cure', 'Disintegration', 1989, 'Goth Rock', 'Dark and atmospheric.'),
    (47, 'Red Hot Chili Peppers', 'Blood Sugar Sex Magik', 1991, 'Funk Rock', 'Funky and melodic.'),
    (48, 'Blink-182', 'Enema of the State', 1999, 'Pop Punk', 'Catchy and energetic.'),
    (49, 'Muse', 'Origin of Symmetry', 2001, 'Alternative Rock', 'Progressive and powerful.'),
    (50, 'Tool', 'Lateralus', 2001, 'Progressive Metal', 'Complex and heavy.')
]
# This code adds multiple rows of album data to a database table in one batch operation.
cur.executemany('''
INSERT INTO albums (rank, artist, album, year, genre, notes)
VALUES (?, ?, ?, ?, ?, ?)
''', albums)

conn.commit()

# Example query to fetch some albums
# cur.execute('SELECT rank, artist, album, year FROM albums ORDER BY rank LIMIT 10')
# rows = cur.fetchall()
# for row in rows:
#     print(row)

def get_albums_by_artist(artist_name):
    cur.execute('SELECT rank, album, year FROM albums WHERE artist = ?', (artist_name,))
    results = cur.fetchall()
    if results:
        for r in results:
            print(f"Rank: {r[0]}, Album: {r[1]}, Year: {r[2]}")
    else:
        print(f"No albums found for artist: {artist_name}")

# === Example usage ===
print("Top 10 albums by rank:")
cur.execute('SELECT rank, artist, album, year FROM albums ORDER BY rank LIMIT 10')
rows = cur.fetchall()
for row in rows:
    print(row)

# print("\nAlbums by Led Zeppelin:")
# get_albums_by_artist('Led Zeppelin')
# get_albums_by_artist('Radiohead')
# get_albums_by_artist('AC/DC')


conn.close()
