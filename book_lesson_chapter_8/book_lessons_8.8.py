def make_album(name_musicant, album, count_ways=None):
    if count_ways:
        music_album = {'name': name_musicant, 'album': album, 'count_ways': count_ways}
    else:
        music_album = {'name': name_musicant, 'album': album}
    return music_album


while True:
    print(f"\nПожалуйста, введите имя музыканта и название альбома.")
    print(f"Для выхода введите 'q'")

    musicant_name = input(f"\nИмя музыканта: ")
    if musicant_name == 'q':
        break

    music_album = input(f"Название альбома: ")
    if musicant_name == 'q':
        break

    album_numb = make_album(musicant_name, music_album)
    print(album_numb)