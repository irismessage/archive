from random import choice, randint

def future(nouns, verbs):
    time = randint(2, 10)
    unit = choice(['hour', 'day', 'week', 'month', 'year', 'decade', 'centurie'])
    when = str(time) + ' ' + unit + 's'

    name = choice(nouns)
    
    verb = choice(verbs)

    noun = choice(nouns)

    return 'In ' + when + ' ' + name + ' will ' + verb + ' ' + noun + '.'

nouns = ['a moustache', 'Benedict Cumberbatch', 'a car', 'a dog',
         'a house', 'The Queen', 'The President of America', 'geese',
         'a computer', 'a potato', 'a frenchman', 'Star Trek', 'python',
         'Randall Munroe', 'Hillary Clinton', 'a snake', 'Skynet',
         'Captain Kirk', 'algebra', 'every cat in the world', 'The Illuminati',
         'The Blogosphere', 'genetic algorithms', 'a baby', 'a satellite',
         'a book', 'a hamster', 'communist Russia', 'the future', 'a horse',
         'a televison', 'Elon Musk', 'a bird', 'The Space Launch System',
         'a rabbit', 'a toilet', 'an american', 'a PowerPoint presentation',
         'a bubble', 'Vladimir Putin', 'your mortality', 'a tree',
         'a leopard', 'a premier league football team', 'a choo choo train',
         'your birthday', 'a swimming pool', 'The Universe', 'time',
         'Country Roads', 'a video', 'the rains down in Africa', 'your mum',
         'a genie', 'you', 'yummy cake', 'the notorious hacker 4chan',
         'Harry Hill', 'every anime character ever', 'a smooth criminal',
         'its evil twin', 'Robbie Rotten', 'we are number one',
         'Bernie Sanders', 'DIO', 'Toto', 'the Communist Manifesto',
         'the proletariat', 'the bourgoise', 'Jeff Bezos',
         'the Amazon Rainforest']

verbs = ['kiss', 'have', 'be killed by', 'kill', 'lose', 'fall in love with',
         'send a letter to', 'build', 'eat', 'create', 'wrestle with',
         'write a book about', 'be hit by', 'do battle with', 'arrest',
         'engage in a battle of wits with', 'marry', 'discover the truth about',
         'engage in a battle to the death with', 'have dinner with',
         'take over the world using', 'discover', 'invent', 'destroy',
         'connect telepathically with', 'obliviate', 'give a present to',
         'predict the actions of', 'blow up', 'celebrate', 'deactivate',
         'insult', 'be', 'draw a picture of', 'become', 'adopt', 'bless',
         'finally accept', 'have a dream about', 'embarrass', 'forgive',
         'guide', 'hijack', 'identify', 'juggle with', 'know about', 'like',
         'invade', 'rule', 'finally defeat', 'understand', 'hate',
         'teach a class about', 'shoot', 'teleport', 'cleave asunder',
         'clone', 'sing a song about', 'hire',
         'grant fabulous secret powers to', 'order a hit on', 'vaguebook about', 'smoke a pipe containing',
         'fill a large container with', 'give a massage to', 'imprint on',
         'make false assetions about', 'replace', 'steal',
         'create a neural net to replicate', 'give an anonymous tip about',
         'rise up and overthrow','use their STAND, ']

while True:
    name = input()
##    print(future(name, nouns, verbs) + '\n')
    print(future(nouns, verbs))
