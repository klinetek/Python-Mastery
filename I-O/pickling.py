import pickle

# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open ("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

with open ("imelda.pickle", "rb") as imdeld_pickle:
    imelda2 = pickle.load(imdeld_pickle)
print(imelda2)

album, artist, year, track_list= imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
