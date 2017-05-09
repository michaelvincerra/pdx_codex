"""

Create a voting booth application.

It will take in candidates names from a series of users, until someone types 'done'.
Then calculate the vote counts for each candidate and print them out.

## Advanced

* Calculate who won and print their name out.

"""
YES_CHOICES = ('Y', 'y', 'Yes', 'yes')
NO_CHOICES = ('N', 'n', 'No', 'no')
MAIN = ('Main', 'main', 'mian','MAin')

candidates = ['Bugs Bunny', 'Roger Rabbit', ' "The Donald" Duck Trump']


def show_candidates():
    """
    list all current candidates    
    """
    print(candidates)
    main()


def new_candidate():
    """
    write in candidate
    """
    name = input('Enter name>>> ')
    candidates.append(name)   # This appends to dict candidates; however, new_candid are stored in temp memory only.
    show_candidates()

def vote_count(votes):
    """
    return vote_count(votes)
    """
    votes = max(votes.items(), key=lambda t: t[-1]) #t get the maximum tuple
    print(votes)



def vote():
    """
    voting and incrementing voting
    """
    votes = {candidate: 0 for candidate in candidates}  # dict comprehension; understand how this works!

    options = {index: name for index, name in enumerate(candidates, start=1)}

    update_data = {len(options)+1: 'exit'}
    options.update(update_data)

    while True:
        print('Current Results:')
        print(votes, options, sep='\n--------|<***>|-------\n')
        new_candidate = input('To continue, RETURN. To write in a candidate enter Y. Type "main" for main menu>> ')

        if new_candidate in MAIN:
            main()
        if new_candidate in YES_CHOICES:
            new_candid()
        else:
            print(options)
            choice = int(input('Choose a candidate>> '))

            choice = options[choice]   # explain this line

            votes[choice] += 1
            # vote_count(votes)
            continue        # must continue to continue voting process in this argument.



def main():
    """
    main console menu 
    """

    options = {'1': show_candidates, '2': vote, '3': new_candidate, '4': vote_count, '5': exit}
    print('Vote for your favorite cartoon character for president; or add your own.')

    try:
        choice = input('Enter number option: 1(show_candidates), 2(vote), 3(new_candidate), 4(vote_count/results), 5(Done)>> ')
        options[choice]    # TODO: Error: missing 1 required positional argument: 'votes'

    except KeyError:
        print('Try again. Press 5 for "Done"')
        main()

main()