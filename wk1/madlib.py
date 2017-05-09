import random as rd


noun = rd.choice(['bloodhound','redneck','white trash', 'victory', 'blashempy', 'bobby pin',
                    'cousin', 'baby doll', 'barn',' fiesta', 'bathroom', 'barbary', 'upset', 'Dilbert',
                    'birdhouse', 'hospital', 'Vatican', 'church', 'baptism', 'bar mitzvah', 'blockbuster film',
                    'politician', 'funeral', 'wedding','torture', 'nunner', 'prep chef', 'thug', 'gangster'])


nouns = rd.choice(['gearheads','rednecks','white trash', 'zealots', 'harlots', 'bobby pins',
                    'cousins', 'baby dolls', 'dunder heads', 'dorks', 'birdhouses', 'haters',
                    'derelicts', 'rascals', 'thieves','criminals', 'cheaters', 'goody two shoes', 'priests'])

verbs = rd.choice(['participate', 'defecate', 'goof-off', 'blaspheme', 'praise', 'waste',
                   'abuse', 'reprimand', 'dangle', 'obliterate', 'dignify', 'disrespect', 'punish',
                   'starve', 'plunder', 'obfuscate', 'slough off', 'squat', 'lounge', 'belittle'])


adjectives = rd.choice(['obtuse', 'besieged', 'forlorn','battered', 'unkempt','horny','playful', 'disastrous','greedy',
                        'pernicious', 'dutiful','pitiful', 'plagued','xenophobic', 'patriotic', 'diabolical','tenacious',
                        'brawny','hefty','threadbare','terrible','amazing','horrifying','lackadaisical', 'chummy',
                        'brotherly','sleepy', 'hungry','artful', 'slick','rico suave', 'careful','caustic','thoughtful',
                        'little-known', 'haughty', 'smarmy', 'obvious','zany', 'nocturnal', 'varnished', 'prenuptial',
                        'hyperbolic', 'bloody', 'spendthrift', 'scheming', 'pretentious', 'powerful', 'smelly', 'naughty'])


blessings = rd.choice(['You shall be honored', 'Yes, indeed', 'Perhaps', 'Sometimes', 'If you apply yourself',
                     'Only on Tuesdays', 'Absolutely', 'Do birds fly?', 'Didn\'t your mother tell you?', 'Open on Mondays',
                     'Emperor Mao agrees', 'Let it be', 'Absolutely!', 'When you\'re wise',
                     'The Dark Lord wills it so', 'On Mars only', 'After or before you die?', 'On Jupiter\'s moons',
                     'For better or worse', 'After immense suffering','Wiser you should be!', 'Barely relevant'])

YES_CHOICE = ('Yes', 'Y', 'y')
NO_CHOICE = ['No', 'N','n']


def maddest(data: str) -> list:
    user_inp2 = input('Enter three adjectives, separated by a comma>> ')
    result = user_inp2.split(',')
    return result

def madder():

    zen = maddest('blah')

    adj_mix = rd.choice(zen)


    print('Based on your interview score, we\'ve developed a job description that best suits you!')
    print(f'Use this carefully crafted career advice to increase your chances of finding a matching job.')

    message2 = f'''
        Behold, {nouns} like you are in high demand.  Therefore, we recommend that you study a {adj_mix} 
        {adjectives} programming language. Skilled job-seekers not only want to {verbs} others in 
        programming, but also emphasize their {noun} and communication skills. {blessings}, you\'re perfectly 
        suited to undertake difficult, {adj_mix} tasks.  However, we caution you to {verbs} in
        your {noun}. Our biometric analysis concludes that you are a very {adj_mix} person with
        a {adjectives} mind. 
        
        Thankfully at PDX Code Guild , you have supportive staff, dedicated teachers and many other 
        {adj_mix} {nouns}. {blessings} my dear job seeker, may the {noun} be with you. 
        '''

    print(message2)


def mad():
    message1 = f'''
    Congratulations! You have been randomly selected to {verbs} our {adjectives} job search 
    process to prepare you for your new career. {blessings}, my friend, you would do well to heed
    this carefully prepared advice. Sit back, take a deep breath, and relax while we calculate your interview score. 
    '''
    print(message1)

    user_inp1 = input('Would you like to proceed? Y/N>> ')

    if user_inp1 in YES_CHOICE:
        madder()
    else:
        print('Thanks for participating!')

mad()