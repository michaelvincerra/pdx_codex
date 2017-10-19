

artists = ("DaVinci", "Rembrandt", "Michelangelo", "Beuys", "Warhol")

for index, artist in enumerate(artists):
    print(index, artist)

# Use 5 if you wish to set a new START INDEX
for index, artist in enumerate(artists, 5):
    print(index, artist)


def enumerator(artists):
    for index, artist in enumerate(artists):
        return
enumerator(artists)
