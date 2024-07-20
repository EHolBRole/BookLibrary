from input_parser import execute_user_input


def get_input():
    user_input = input().split()
    return user_input


def main():
    execute_user_input(get_input())


main()
