board = {'7':' ','8':' ','9':' ',
         '4':' ','5':' ','6':' ',
         '1':' ','2':' ','3':' '
}
board_keys = []
for key in board:
    board_keys.append(key)
def display(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        display(board)
        print(f'Its your turn {turn} .Move to which place?')
        move = input().upper()
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print('That Place is already taken!\n Move to which placee?')
            continue
        if count >= 5:
            if board['7'] == board['8'] == board['9']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['4'] == board['5'] == board['6']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['1'] == board['2'] == board['3']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['7'] == board['5'] == board['3']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['9'] == board['5'] == board['1']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['1'] == board['4'] == board['7']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['2'] == board['5'] == board['8']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
            elif board['3'] == board['6'] == board['9']:
                display(board)
                print("\nGame Over!\n")
                print(f'{turn} won!')
                break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do you want to play agan?y/n: ")
    if restart.lower() == 'y':
        for key in board:
            board[key] = " "
        game()
if __name__ == "__main__":
    game()
