def make_album(name_musicant, album, count_ways=None):
    if count_ways:
        music_album = {'name': name_musicant, 'album': album, 'count_ways': count_ways}
    else:
        music_album = {'name': name_musicant, 'album': album}
    return music_album



album_1 = make_album('Elvis Presley', 'Mamochita')
print(album_1)
album_2 = make_album('Aniston Ashley', 'Garmoniya')
print(album_2)
album_3 = make_album('Bill Moris', 'Canchita')
print(album_3)
album_4 = make_album('Bill Moris', 'Canchita', '15')
print(album_4)