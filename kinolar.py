"""01.07.2022 yil
mavzu: doc_string"""
'____________________________''* astris:manosini bildiradi'
"""Movie_kino.my:"""

# def daraja(x: float , y : float):
#     """
#     sonni darajasi hisoblash
#
#     :param x:
#     :param y:
#     :return:
#     """
#
#     return x**y
# print(daraja(2,5))

films =['Avangars','Forsaj','Titanik','Ono','Anabella','Avatar','Sonic','Mateix'
        ]
print(films)
while True:
    command = input("Add,Insert,Delete\nChoice command: ")
    movieName = input('Movie: ')
    try:
        if command=='Add':
            films.append(movieName)
        elif command =='Insert':
            index = int(input('Index:'))
            films.insert(index,movieName)
        elif command=='Delete':
            films.remove(movieName)
    except:
        print('cann not found film name')
    print(films)

# def echo(*args):
#     return args
# print(echo('salom','qaleysiz','hello','bik','dens'))