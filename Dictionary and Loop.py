vocabs = {}


type(vocabs)

vocabs['programming'] = 'the activity of job of writing computer programs'
vocabs


vocabs['python'] = 'a very large snake that kills animals for food'

del(vocabs['programming'])

vocabs.clear()

vocabs['programming'] = ['the activity of job of writing computer programs','_______ming']

vocabs = {'programming': 'the activity of job of writing computer programs',
          'python': 'a very large snake'}


vocabs = {'programming': ['the activity or job of writing computer programs','_______ming'],
          'python': ['a very large snake that kills animals for food by wrapping itself around them and crushing them', '___hon'],
          'fun': ['pleasure, enjoyment, or entertainment', '__n']}

vocabs.keys()

vocabs.values()

vocabs.items()

for key in vocabs.keys():
    print(key)

for value in vocabs.values():
    print(value)

for key,value in vocabs.items():
    print('{} ({})\n  {}'.format(key,value[1],value[0]))
