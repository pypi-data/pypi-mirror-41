import argparse
import webbrowser
from jovian.utils.api import get_key
from jovian.utils.credentials import purge_config
from jovian.utils.clone import clone


def exec_clone(slug):
    clone(slug)


def exec_init():
    print('[jovian] Visit https://app.jovian.ai to sign up and generate an API key.')
    # webbrowser.open('https://jvn.io/')
    purge_config()
    get_key()
    print('Credentials validated and saved to ~/.jovian/credentials.json.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('gist', nargs='?')

    args = parser.parse_args()
    command = args.command
    if command == 'init':
        exec_init()
    elif command == 'clone':
        if not args.gist:
            print('Please provide the Gist ID to clone')
            return
        exec_clone(args.gist)


if __name__ == '__main__':
    main()
