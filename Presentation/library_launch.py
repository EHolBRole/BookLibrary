import json

import Exceptions.exceptions as ex
import Presentation.input_mapper as im
import Presentation.response_handler as rh


def get_input():
    user_input = input().split()
    return user_input


def main():
    is_to_continue = True
    while is_to_continue:
        try:
            response = im.premap_user_input(get_input())
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
        except ex.ExitCommandException:
            print('Sorry, you shouldn\'t add any arguments to exit command!')
        except json.JSONDecodeError:
            print("Sorry, JSON file is either empty or broken!")
        except ex.FinishInterpretationException:
            print('Thank you!')
            is_to_continue = False


# main()
