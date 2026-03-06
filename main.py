from game.human_player import HumanPlayer
from game.computer_player import ComputerPlayer
from game.reversi_game import ReversiGame
from game.reversi_game import BLACK_SYMBOL
from game.reversi_game import BLACK_COLOR
from game.reversi_game import WHITE_SYMBOL
from game.reversi_game import WHITE_COLOR
from game.game_mode import GameMode

# GAME_MODE = 3  # 0 - HumanPlayer vs HumanPlayer, 1 - HumanPlayer vs ComputerPlayer, 2 - ComputerPlayer vs HumanPlayer, 3 - ComputerPlayer vs ComputerPlayer
ITERATIONS = 10

while True:
    user_input = input(
        "Welcome to game Reversi! Please select your Game Mode and enjoy your game!\n"
        "0 - Human vs Human\n"
        "1 - Human vs Computer\n"
        "2 - Computer vs Human\n"
        "3 - Computer vs Computer\n"
        "Type QUIT to exit.\n"
        "Game Mode: "
    ).strip().upper()

    if user_input == "QUIT":
        print("Goodbye!")
        break

    try:
        game_mode = GameMode(int(user_input))
        print(f"You selected: {game_mode.name}")
    except ValueError:
        print("Invalid choice. Please enter a number (0-3) or type QUIT to exit.")
        continue

    match game_mode.name:
        case "HUMAN_HUMAN":
            print('HumanPlayer vs HumanPlayer')
            g = ReversiGame(6, HumanPlayer(BLACK_SYMBOL, BLACK_COLOR),
                            HumanPlayer(WHITE_SYMBOL, WHITE_COLOR))

        case "HUMAN_COMPUTER":
            print('HumanPlayer vs ComputerPlayer')
            g = ReversiGame(6, HumanPlayer(BLACK_SYMBOL, BLACK_COLOR),
                            ComputerPlayer(WHITE_SYMBOL, 1))

        case "COMPUTER_HUMAN":
            print('ComputerPlayer vs HumanPlayer')
            g = ReversiGame(6, ComputerPlayer(BLACK_SYMBOL, 1),
                            HumanPlayer(WHITE_SYMBOL, WHITE_COLOR))

        case "COMPUTER_COMPUTER":
            print('ComputerPlayer vs ComputerPlayer')
            g = ReversiGame(6, ComputerPlayer(BLACK_SYMBOL, 0),
                            ComputerPlayer(WHITE_SYMBOL, 0))

            # print('ComputerPlayer vs ComputerPlayer')
            # black_wins: int = 0
            # black_total_points: int = 0
            # black_points: int = 0
            # white_wins: int = 0
            # white_total_points: int = 0
            # white_points: int = 0

            # for i in range(ITERATIONS):
            #     g = ReversiGame(6, ComputerPlayer(BLACK_SYMBOL, 0),
            #                     ComputerPlayer(WHITE_SYMBOL, 0))

            # black_points, white_points = g.play()
            # g.play()

            # black_total_points += black_points
            # white_total_points += white_points

            # if (black_points > white_points):
            #     black_wins += 1

            # if (black_points < white_points):
            #     white_wins += 1

            # print(black_wins, white_wins, ITERATIONS - black_wins - white_wins)
            # print(black_total_points, white_total_points)

        case _:
            print("You might have selected invalid Game Mode. Please try again!")
            continue

    g.play()
    break
