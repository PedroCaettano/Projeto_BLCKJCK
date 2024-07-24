import random
from replit import clear
from art import logo

def deal_card():
    """Uma carta randômica é adicionada ao Deck"""
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta

def calculate_score(cartas):
    """Aqui está a lista de cartas e o retorno calculado delas"""
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0

    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Você deu o seu melhor, parceiro. Mas você perdeu."

    if user_score == computer_score:
        return "Empate!"
    elif computer_score == 0:
        return "Você perdeu! Seu oponente tirou 21!"
    elif user_score == 0:
        return "Você venceu com um belo 21!"
    elif user_score > 21:
        return "Você deu o seu melhor, mas você perdeu."
    elif computer_score > 21:
        return "Seu oponente perdeu. Você venceu!"
    elif user_score > computer_score:
        return "Você venceu!"
    else:
        return "Você perdeu..."

def play_game():
    print(logo)

    user_cartas = []
    computer_cartas = []
    game_over = False

    for _ in range(2):
        user_cartas.append(deal_card())
        computer_cartas.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cartas)
        computer_score = calculate_score(computer_cartas)
        print(f"Suas cartas: {user_cartas}, esta é a sua pontuação: {user_score}")
        print(f"A primeira carta do computador: {computer_cartas[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Aperte 's' para receber uma carta, ou aperte 'n' para passar a vez: ")
            if user_should_deal == "s":
                user_cartas.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cartas.append(deal_card())
        computer_score = calculate_score(computer_cartas)

    print(f"Sua última mão: {user_cartas}, sua pontuação é {user_score}")
    print(f"A mão final do computador é: {computer_cartas}, sua pontuação final é {computer_score}")
    print(compare(user_score, computer_score))

while input("Tá afim de testar a sorte e jogar 21? Digite 's' ou 'n': ") == "s":
    clear()
    play_game()
