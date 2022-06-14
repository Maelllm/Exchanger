import json

with open('vault.txt') as json_file:  # Will use json type to operate with dictionaries
    vault = json.load(json_file)


def start():
    user_command: str = input('COMMAND? \n')  # Users command
    command_list: list = user_command.split()

    def stop():
        print('SERVICE STOPPED')
        with open('vault.txt', 'w') as outfile:  # Need to save new values
            global vault
            json.dump(vault, outfile)
        exit()

    if len(command_list) > 1:  # Assign currency and command
        currency: str = command_list[1].upper()
        command: str = command_list[0].lower()
    elif command_list[0].lower() == 'stop':  # Some exception for stop command
        stop()
    else:
        print('Enter valid command')
        start()
    if len(command_list) >= 3:  # Required for amount of currency for exchange
        amount_money: int = int(command_list[2])
    if currency != "USD" and currency != "UAH":
        print(f'INVALID CURRENCY {currency}')
        start()
    usd_v: dict = vault['currencies'][0]
    uah_v: dict = vault['currencies'][1]

    def course():
        if currency == 'USD':
            return f'RATE {usd_v["curr_rate"]}, AVAILABLE {round(usd_v["curr_amount"], 2)}'
        elif currency == 'UAH':
            return f'RATE {uah_v["curr_rate"]}, AVAILABLE {round(uah_v["curr_amount"], 2)}'

    def exchange():  # Need to be careful with correct courses using (logic is not so intuitive)
        if currency == 'USD':  # When you exchange USD you need to look in uah amount and vice versa
            if amount_money * uah_v["curr_rate"] <= uah_v["curr_amount"]:
                usd_v["curr_amount"] += amount_money
                uah_v["curr_amount"] -= amount_money * uah_v["curr_rate"]
                return f'UAH {round(amount_money * uah_v["curr_rate"], 2)}, RATE {uah_v["curr_rate"]}'
            else:
                return f' UNAVAILABLE, REQUIRED BALANCE UAH {amount_money * uah_v["curr_rate"]},' \
                       f' AVAILABLE {round(uah_v["curr_amount"], 4)}'
        elif currency == 'UAH':
            if amount_money / usd_v["curr_rate"] <= usd_v["curr_amount"]:
                uah_v["curr_amount"] += amount_money
                usd_v["curr_amount"] -= amount_money / usd_v["curr_rate"]
                return f'USD {round(amount_money / usd_v["curr_rate"], 2)}, RATE {round(1 / usd_v["curr_rate"], 6)}'
            else:
                return f' UNAVAILABLE, REQUIRED BALANCE USD {round(amount_money / usd_v["curr_rate"], 4)}, ' \
                       f'AVAILABLE {round(usd_v["curr_amount"], 4)}'

    functions: dict = {'course': course, 'exchange': exchange, 'stop': stop}  # Setup predicted functions
    try:
        print(functions[command]())
    except:
        print(f'No {command} command found')
        start()  # If command does not exist - start again
    start()  # When command finished - start again


if __name__ == "__main__":
    start()
