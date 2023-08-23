WITHDR_MIN_LIM = 30
WITHDR_MAX_LIM = 600
balance = 0
withdraw_fee = 0
op_count = 0
BONUS_3_OPS = balance * 0.03
WEALTH_FEE = balance * 0.1

while True:
    if op_count == 3:
        balance += BONUS_3_OPS
    if balance > 5000000:
        balance -= WEALTH_FEE
    action = input('Enter operation command (i - insert, w - withdraw, b = balance, q = quit): ')
    if action == 'i':
        insert_sum = int(
            input('Sum you are about to insert should be multiple to 50. Please enter the sum to insert: '))
        if insert_sum % 50 == 0:
            balance += insert_sum
            op_count += 1
            print(f'Your balance makes - {balance}')
        else:
            print('Sum you are about to insert should be multiple to 50. Please try again')
    elif action == 'w':
        withdrawal_sum = int(
        input('Sum you are about to withdraw should be multiple to 50. Please enter the sum to withdraw: '))
        withdrawal_fee = withdrawal_sum * 0.015
        if withdrawal_fee < WITHDR_MIN_LIM:
            withdrawal_fee = WITHDR_MIN_LIM
        if withdrawal_fee > WITHDR_MAX_LIM:
            withdrawal_fee = WITHDR_MAX_LIM
        if withdrawal_sum % 50 == 0 and withdrawal_sum < balance:
            balance -= withdrawal_sum
            op_count += 1
            print(f'Your balance makes - {balance - withdrawal_fee}')
        else:
            if withdrawal_sum % 50 != 0:
                print('Sum you are about to withdraw should be multiple to 50')
            else:
                print('Sorry, entered sum prevails your balance')
    elif action == 'q':
        print('Hope to see you again')
    elif action == 'b':
        print(f'Your current balance = {balance}')
    else:
        print('Unknown command. Please try again')
        break

