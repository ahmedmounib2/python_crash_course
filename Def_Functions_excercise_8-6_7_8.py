# excercise 8-6

def city_country(city_name,country_name):
    """return a string of the city name"""
    full_name = f'"{city_name}, {country_name}"'
    return full_name.title()

city0 = city_country('cairo','egypt')
print(city0)

city1 = city_country(city_name='NYC',country_name='usa')
print(city1)
city2 = city_country(country_name='lala land',city_name='mars')
print(city2)
city3 = city_country(city_name='paris',country_name='france')
print(city3)

def make_album(artist_name,album_title,songs_number= ''):
    """make a dictionary about the album and the artist name"""
    album = {'artist name':artist_name,'album title':album_title}
    if songs_number:
        album['number of songs']= songs_number
    return album

mounir = make_album('mohamed mounir','bnetweled',12)
print(mounir)

hamaky = make_album(album_title= 'hekayet wakt',artist_name= 'mohamed hamaky')
print(hamaky)

amr = make_album('amr diab',album_title= 'habibit alby', songs_number= 13)
print(amr)

def user_album(artist,album,songs_number = ''):
    """prompt users to store their favorite artists in a dictionary"""
    favorite_album = {'Artist Name':artist,'Album Name':album}
    if songs_number:
        favorite_album['Total number of Songs']: songs_number
        return favorite_album

while True:
    print("\nWrite 'q' to quit anytime.")
    art_name = input("Whats your favorite artist: ")
    if art_name == 'q':
        break
    alb_name = input("which album: ")
    if alb_name == 'q':
        break
    favorite_album = {'Artist Name':art_name,'Album Name':alb_name}
    print(favorite_album)
