import random


class Card:
    def __str__(self):
        numbers = [el for el in range(1, 91)]
        line_1 = []
        line_2 = []
        line_3 = []
        i = 0
        while i < 5:
            number = random.choice(numbers)
            line_1.append(number)
            i += 1
            numbers.remove(number)
        i = 0
        while i < 5:
            number = random.choice(numbers)
            line_2.append(number)
            i += 1
            numbers.remove(number)
        i = 0
        while i < 5:
            number = random.choice(numbers)
            line_3.append(number)
            i += 1
            numbers.remove(number)
        line_1 = sorted(line_1)
        line_2 = sorted(line_2)
        line_3 = sorted(line_3)
        line_1_str = []
        line_2_str = []
        line_3_str = []

        for i_1 in range(4):
            line_1.insert(random.choice(range(9)), '  ')
        for el in line_1:
            line_1_str.append(str(el))
            for p_1 in range(10):
                if f'{p_1}' in line_1_str:
                    line_1_str[line_1_str.index(f'{p_1}')] = f' {p_1}'
        str_1 = ' '.join(line_1_str)

        for i_2 in range(4):
            line_2.insert(random.choice(range(9)), '  ')
        for el in line_2:
            line_2_str.append(str(el))
        for p_2 in range(10):
            if f'{p_2}' in line_2_str:
                line_2_str[line_2_str.index(f'{p_2}')] = f' {p_2}'

        str_2 = ' '.join(line_2_str)

        for i_3 in range(4):
            line_3.insert(random.choice(range(9)), '  ')
        for el in line_3:
            line_3_str.append(str(el))
        for p_3 in range(10):
            if f'{p_3}' in line_3_str:
                line_3_str[line_3_str.index(f'{p_3}')] = f' {p_3}'
        str_3 = ' '.join(line_3_str)
        return f'---------------------------\n{str_1}\n{str_2}\n{str_3}'


class Loto:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

    def start(self):
        computer_score = 0
        player_score = 0
        lose = False
        numbers_list = [el for el in range(1, 91)]
        human_list = str(self.human_player).split('\n')
        computer_list = str(self.computer_player).split('\n')
        while True:
            user_card = '\n'.join(human_list)
            computer_card = '\n'.join(computer_list)
            print(f'Карточка игрока:\n {user_card}')
            print(f'Карточка компьютера :\n {computer_card}')
            random_number = random.choice(numbers_list)
            print(f'Новый бочонок: {random_number} Осталось {len(numbers_list) - 1}')
            numbers_list.remove(random_number)
            request = input('Зачеркнуть цифру? Y/N ')
            if request == 'Y':
                lose = True
                if len(str(random_number)) == 2:
                    for i in range(len(human_list)):
                        if str(random_number) in human_list[i]:
                            human_list[i] = human_list[i].replace(str(random_number), '- ')
                            player_score += 1
                            lose = False
                if len(str(random_number)) == 1:
                    for i in range(len(human_list)):
                        if f' {str(random_number)} ' in human_list[i]:
                            human_list[i] = human_list[i].replace(f' {str(random_number)} ', ' - ')
                            player_score += 1
                            lose = False
                if lose == True:
                    print('Вы проиграли')
                    break
            if len(str(random_number)) == 2:
                for i in range(len(computer_list)):
                    if str(random_number) in computer_list[i]:
                        computer_list[i] = computer_list[i].replace(str(random_number), '- ')
                        computer_score += 1
            if len(str(random_number)) == 1:
                for i in range(len(computer_list)):
                    if f' {str(random_number)} ' in computer_list[i]:
                        computer_list[i] = computer_list[i].replace(f' {str(random_number)} ', ' - ')
                        computer_score += 1
            if computer_score == 15:
                print('Победил компьютер')
                break
            if player_score == 15:
                print('Вы победили')
                break


a = Card()
b = Card()
c = Loto(a, b)
c.start()
