import copy
import random
import pyautogui
import list_of_moves


def find_moves():
    moves_list = []
    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            moves_list.append(str(i + 1))
    return moves_list


def make_move():
    global mark
    legal_moves = find_moves()
    for i in legal_moves:
        if move == i:
            board[int(move) - 1] = mark


def check_win():
    # Horizontal Check
    for x in range(3):
        countx = 0
        county = 0
        for i in board[x * 3:(x * 3) + 3]:
            if i == "X":
                countx += 1
                if countx == 3:
                    return 10
            elif i == "O":
                county += 1
                if county == 3:
                    return -10
    # Diagonal Check
    if (board[0] == board[4] == board[8] and board[0] == "X") or (board[2] == board[4] == board[6] and board[2] == "X"):
        return 10
    elif (board[0] == board[4] == board[8] and board[0] == "O") or (
            board[2] == board[4] == board[6] and board[2] == "O"):
        return -10
    # Vertical Check
    for i in range(3):
        if board[0:3][i] == board[3:6][i] == board[6:9][i] and board[i] == "X":
            return 10
        elif board[0:3][i] == board[3:6][i] == board[6:9][i] and board[i] == "O":
            return -10

    for i in board:
        if i != "X" and i != "O":
            return 1  # check for possible moves
    return False  # draw


all_moves = list_of_moves.moves
p2_allmoves = list_of_moves.moves2
game = 0
while True:
    if pyautogui.position().x < 100:
        break
    for z in range(1000):
        game += 1
        board = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9", ]
        # board[random.randint(0, 8)] = "X"
        run = True
        p1_turn = True
        mark = None
        game_moves = []
        game_moves2 = []
        while run:
            print()
            print(board[0:3])
            print(board[3:6])
            print(board[6:9])
            print()

            move_list = find_moves()
            if p1_turn:
                possible_boards2 = []
                best_move2 = []
                # for i in board:
                #     if i != "X" and i != "O":
                #         fake = copy.copy(board)
                #         fake[fake.index(i)] = "X"
                #         possible_boards2.append(''.join(fake))
                #     else:
                #         possible_boards2.append(-1000000)
                # for i in possible_boards2:
                #     if i not in p2_allmoves and i != -1000000:
                #         best_move2.append(1)
                #     elif i == -1000000:
                #         best_move2.append(-1000000)
                #     else:
                #         best_move2.append(p2_allmoves[p2_allmoves.index(i) + 1] / p2_allmoves[p2_allmoves.index(i) + 2])
                # move = str(best_move2.index(max(best_move2)) + 1)
                # move = move_list[random.randint(0, len(move_list) - 1)]
                move = input("Choose Your Move: ")
                if move == "stop":
                    print(all_moves)
                    print(len(all_moves))
                    print(p2_allmoves)
                    print(len(p2_allmoves))
                mark = "X"
                make_move()
                game_moves2.append(copy.copy("".join(board)))
                p1_turn = False
            else:
                possible_boards = []
                best_move = []
                for i in board:
                    if i != "X" and i != "O":
                        fake = copy.copy(board)
                        fake[fake.index(i)] = "O"
                        possible_boards.append(''.join(fake))
                    else:
                        possible_boards.append(-1000000)
                for i in possible_boards:
                    if i not in all_moves and i != -1000000:
                        best_move.append(1)
                    elif i == -1000000:
                        best_move.append(-1000000)
                    else:
                        best_move.append(all_moves[all_moves.index(i) + 1] / all_moves[all_moves.index(i) + 2])
                move = str(best_move.index(max(best_move)) + 1)
                # move = move_list[random.randint(0, len(move_list) - 1)]
                mark = "O"
                make_move()
                game_moves.append(copy.copy("".join(board)))
                p1_turn = True

            # CHECK FOR WIN
            win = check_win()
            if win != 1:
                # P1 wins
                if win == 10:
                    print("P1 wins")
                    for i in game_moves:
                        if i not in all_moves:
                            all_moves.append(i)
                            all_moves.append(0.9)
                            all_moves.append(1)
                        else:
                            all_moves[all_moves.index(i) + 2] += 0.3
                    for i in game_moves2:
                        if i not in p2_allmoves:
                            p2_allmoves.append(i)
                            p2_allmoves.append(1)
                            p2_allmoves.append(1)
                        else:
                            p2_allmoves[p2_allmoves.index(i) + 1] += 0.1
                            p2_allmoves[p2_allmoves.index(i) + 2] += 0.1
                # P2 wins
                elif win == -10:
                    print("P2 wins")
                    for i in game_moves:
                        if i not in all_moves:
                            all_moves.append(i)
                            all_moves.append(1)
                            all_moves.append(1)
                        else:
                            all_moves[all_moves.index(i) + 1] += 0.1
                            all_moves[all_moves.index(i) + 2] += 0.1
                    for i in game_moves2:
                        if i not in p2_allmoves:
                            p2_allmoves.append(i)
                            p2_allmoves.append(0.9)
                            p2_allmoves.append(1)
                        else:
                            p2_allmoves[p2_allmoves.index(i) + 2] += 0.3
                # Draw
                elif not win:
                    print("Draw")
                    for i in game_moves:
                        if i not in all_moves:
                            all_moves.append(i)
                            all_moves.append(1)
                            all_moves.append(1)
                        else:
                            all_moves[all_moves.index(i) + 1] += 0.085
                            all_moves[all_moves.index(i) + 2] += 0.1
                    for i in game_moves2:
                        if i not in p2_allmoves:
                            p2_allmoves.append(i)
                            p2_allmoves.append(1)
                            p2_allmoves.append(1)
                        else:
                            p2_allmoves[p2_allmoves.index(i) + 1] += 0.075
                            p2_allmoves[p2_allmoves.index(i) + 2] += 0.1
                run = False
                print(game)
        print()
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])


print(all_moves)
print(len(all_moves))
print(p2_allmoves)
print(len(p2_allmoves))


