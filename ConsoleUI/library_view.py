import Exceptions.exceptions as ex

from input_parser import execute_user_input

def get_input():
    user_input = input().split()
    return user_input


def main():
    try:
        execute_user_input(get_input())
    except ex.AddCommandException:
        print('Sorry, you\'ve entered wrong arguments!')
    except ex.RemoveCommandException:
        print('Sorry, you\'ve entered wrong arguments!')
    except ex.FindCommandException:
        print('Sorry, you\'ve entered wrong arguments!')
    except ex.ChangeCommandException:
        print('Sorry, you\'ve entered wrong arguments!')
    except ex.ShowCommandException:
        print('Sorry, you\'ve entered wrong arguments!')
    except ex.IncorrectCommandException:
        print('Sorry, you\'ve entered unknown command!')


main()
