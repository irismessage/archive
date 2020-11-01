from time import time

def sign_of_the_cross():
    raise ModuleNotFoundError('Do not have arms.')

apostles_creed = ('I believe in God, the Father almighty, \n'
                  'creator of heaven and earth. \n'
                  'I believe in Jesus Christ, God\'s only Son, our Lord, \n'
                  'who was conceived by the Holy Spirit, \n'
                  'born of the Virgin Mary, \n'
                  'suffered under Pontius Pilate, \n'
                  'was crucified, died, and was buried; \n'
                  'he descended to the dead. \n'
                  'On the third day he rose again; \n'
                  'he ascended into heaven, \n'
                  'he is seated at the right hand of the Father, \n'
                  'and he will come to judge the living and the dead. \n'
                  'I believe in the Holy Spirit, \n'
                  'the holy catholic Church, \n'
                  'the communion of saints, \n'
                  'the forgiveness of sins, \n'
                  'the resurrection of the body, \n'
                  'and the life everlasting. Amen.')

our_father = ('Our Father who art in heaven, \n'
              'Hallowed be thy name. \n'
              'Thy kingdom come. \n'
              'Thy will be done \n'
              'on earth as it is in heaven. \n'
              'Give us this day our daily bread, \n'
              'and forgive us our trespasses, \n'
              'as we forgive those who trespass against us, \n'
              'and lead us not into temptation, \n'
              'but deliver us from evil.')

hail_mary = ('Hail Mary, full of grace, \n'
             'the Lord is with thee; \n'
             'blessed art thou amongst women, \n'
             'and blessed is the fruit of thy womb, Jesus. \n'
             'Holy Mary, Mother of God, \n'
             'pray for us sinners, \n'
             'now and at the hour of our death. Amen.')

glory_be = ('Glory to the Father, and to the Son, and to the Holy Spirit, \n'
            'As it was in the beginning, and now, and ever shall be, '
            'world without end. Amen.')

def start():
    try:
        sign_of_the_cross()
    except:
        pass
    print(apostles_creed)
    print(our_father)
    for i in range(3):
        print(hail_mary)
    print(glory_be)

def decade(mystery):
    print(mystery)
    print(our_father)
    for i in range(10):
        print(hail_mary)
    print(glory_be)
    try:
        sign_of_the_cross()
    except:
        pass

mysteries = {'Joyful Mysteries': ['The Annunciation',
                                  'The Visitation',
                                  'The Nativity',
                                  'The Presentation of Jesus at the Temple',
                                  'The Finding of Jesus in the Temple'],
             'Sorrowful Mysteries': ['The Agony in the Garden',
                                     'The Scourging at the Pillar',
                                     'The Crowning with Thorns',
                                     'The Carrying of the Cross',
                                     'The Crucifixion and Death of our Lord'],
             'Glorious Mysteries': ['The Resurrection',
                                    'The Ascension',
                                    'The Descent of the Holy Spirit',
                                    'The Assumption of Mary',
                                    'The Coronation of the Virgin']}


start_time = time()

start()
for set in list(mysteries):
    for mystery in set:
        decade(mystery)
        
end_time = time()
time_taken = end_time - start_time

print('\n Finished Rosary in ' + str(time_taken) + ' seconds.')

