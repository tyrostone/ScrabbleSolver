from solver.solver import ScrabbleSolver


def main(rack):
    s = ScrabbleSolver(rack)
    print s.score()


if __name__ == '__main__':
    print('Press CTRL+C to exit')
    while True:
        try:
            rack = raw_input("Enter a rack: ")
            main(str(rack))
        except ValueError:
            print("No words found given the specified rack")
        except KeyboardInterrupt:
            print('\nExiting! Goodbye :)')
            break
