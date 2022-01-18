import time

from pyfiglet import Figlet

def main():
    print("Hello World, thats the initial commit")
    time.sleep(3)
    f = Figlet(font='slant')
    print(f.renderText(f'Spotify to YouTube Music'))


if __name__ == "__main__":
    main()