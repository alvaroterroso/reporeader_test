#Álvaro Terroso
#2021213782

#Hugo Neves
#2022214562

import time
import random
import functools
import turtle

MAX_X = 600
MAX_Y = 800
DEFAULT_SIZE = 20
SNAKE_SHAPE = 'square'
HIGH_SCORES_FILE_PATH = 'high_scores.txt'
SPEED = 0.12 #velocidade da turtle/jogo

def init_map(color):
    turtle.speed(0)
    turtle.up()
    turtle.goto(-300, 400)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(600)
        turtle.right(90)
        turtle.fd(800)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0, 0)
    turtle.hideturtle()

def load_high_score(state):

    #esta função permite-nos ver se existe algum high_score no ficheiro

    high_score = [0] # inicializazação da lista auxiliar a 0, pois se o contéudo do ficheiro estiver vazio, o state['high_score'] é 0
    f = open(HIGH_SCORES_FILE_PATH, 'a+')
    lines = len(f.readlines()) #ver quantas linhas o ficheiro tem
    f.seek(0) #para ter uma abordagem segura, relocalizar o ponteiro de leitura ao início
    for i in range(lines):
        aux = f.readline() #variável auxiliar que guarda uma linha de cada vez
        for i in range(len(aux)):#percorre o conteúdo dessa linha
            if aux[i] == " ":#se o caracter em questão for um espaço
                high_score_aux = aux[(i+1):]#guardar o resto do conteúdo da string como o high_score em str
                high_score_aux2 = int(high_score_aux)#conversão de str para int
                high_score.append(high_score_aux2)#adicionar esse valor à lista
    biggest_hs = high_score[0]
    for i in high_score:#ciclo para descobrir o valor maior
        if i > biggest_hs:
            biggest_hs = i

    state['high_score'] = biggest_hs#guardar o maior valor como high_score
    f.close()#fechar o ficheiro (boa prática)
    update_score_board(state)
    pass

def write_high_score_to_file(state):

    #caso haja um highscore, escreve-o no ficheiro
    f = open(HIGH_SCORES_FILE_PATH, 'a')#abertura em append para adicionar sem eliminar o conteúdo do ficheiro
    name = str(input("NAME:"))#pedir o nome ao jogador
    player = name + " " + str(state['high_score']) + "\n" #criar a variável com o design desejado
    f.write(player)#escrever no ficheiro
    f.close()#fechar o mesmo (boa prática)
    pass

def create_score_board(state):

    #setup da scoreboar pré - feito
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.shape("square")
    score_board.color("black")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, MAX_Y / 2.2)
    state['score_board'] = score_board
    load_high_score(state)
    update_score_board(state)

def update_score_board(state):

    #função pré feita

    state['score_board'].clear()
    state['score_board'].write("Score: {} High Score: {}".format(state['score'], state['high_score']), align="center", font=("Helvetica", 24, "normal"))

def go_up(state):
    if state['snake']['current_direction'] != 'down':
        state['snake']['current_direction'] = 'up'


def go_down(state):
    if state['snake']['current_direction'] != 'up':
        state['snake']['current_direction'] = 'down'

def go_left(state):
    if state['snake']['current_direction'] != 'right':
        state['snake']['current_direction'] = 'left'

def go_right(state):
    if state['snake']['current_direction'] != 'left':
        state['snake']['current_direction'] = 'right'

def init_state():
    state = {}

    state['score_board'] = None
    state['new_high_score'] = False
    state['high_score'] = 0
    state['score'] = 0
    state['food'] = None
    state['window'] = None

    snake = {
        'head': None,
        'body': [], # criação de uma lista onde se armazenam todas as turtles pertencentes ao corpo
        'current_direction': None

    }
    state['snake'] = snake
    return state

def check_high_score(state):

    #verificar se o score do jogador é maior que aquele registado no ficheiro

    if state['score'] > state['high_score']:
        state['high_score'] = state['score']
        state['new_high_score'] = True

def setup(state):
    window = turtle.Screen()
    window.setup(width=MAX_X, height=MAX_Y)
    window.listen()
    window.onkey(functools.partial(go_up, state), 'Up')
    window.onkey(functools.partial(go_down, state), 'Down')
    window.onkey(functools.partial(go_left, state), 'Left')
    window.onkey(functools.partial(go_right, state), 'Right')
    window.tracer(0)
    state['window'] = window
    snake = state['snake']
    snake['current_direction'] = 'stop'
    snake['head'] = turtle.Turtle()
    snake['head'].shape(SNAKE_SHAPE)
    snake['head'].showturtle()
    snake['head'].pu()
    snake['head'].color('green')
    create_score_board(state)
    create_food(state)

def move(state):

    #Função que diz respeito à movimentação da turtle

    snake = state['snake'] # inicilizar variável snake para ter uma escrita mais curta

    if (snake['current_direction'] == 'up'):
        snake['head'].setheading(90) #dar à turtle a orientação certa
        snake['head'].fd(DEFAULT_SIZE)#mexer a quantidade de unidades pré-definida

    if (snake['current_direction'] == 'down'):
        snake['head'].setheading(-90)
        snake['head'].fd(DEFAULT_SIZE)

    if (snake['current_direction'] == 'right'):
        snake['head'].setheading(0)
        snake['head'].fd(DEFAULT_SIZE)

    if (snake['current_direction'] == 'left'):
        snake['head'].setheading(180)
        snake['head'].fd(DEFAULT_SIZE)

def create_food(state):

    #função que cria comida e representa-a no mapa

    x = random.randint(int(-(MAX_X/2)+DEFAULT_SIZE), int((MAX_X/2)-DEFAULT_SIZE))
    y = random.randint(int((-MAX_Y/2)+DEFAULT_SIZE), int((MAX_Y/2)-DEFAULT_SIZE))
    food = turtle.Turtle() #a comida é também uma turtle
    food.color('red')
    food.shape('circle')
    food.shapesize(0.5)
    food.up()
    food.goto(x,y) #direacionar a comida para as localizações random criadas
    state['food'] = food #alterar no dicionário o valor da key food para a respetiva turtle
    check_high_score(state) #verificar se o score é maior que o high_score

def add_body(state):

    # função com utilidade de adicionar corpo após o contacto com uma comida

    body = state['snake']['body']
    new_body = turtle.Turtle() #criação de uma nova turtle
    new_body.shape(SNAKE_SHAPE)#setup igual à cabeça
    new_body.color('black')#apenas é diferente a sua cor
    new_body.pu()
    body.append(new_body)#adicionar à lista no dicionário a nova turtle criada

def move_body(state):

    #função responsável pelo movimento do corpo

    body = state['snake']['body']
    head = state['snake']['head']

    for i in range(len(body) - 1, -1, -1):  #leitura da lista de turtles de trás para a frente (adicionando -1 invés de +1)
        #primeiro parametro do for significa a quantidade de vezes que o ciclo roda; o 2º é onde começa, o 3º quanto ele soma ao i (no caso + (-1))
        if i == 0:
            body[i].goto(head.pos())# a primeira turtle irá herdar a última posição da cabeça
        else:
            body[i].goto(body[i-1].pos())#todas as outras erão herdar a posições da turtle a seguir, isto é, body[-1] irá herdar a posição de body[-2]


def check_if_food_to_eat(state):

    #verificação se existe alguma colisão entre a cabeça e a comida

    snake = state['snake']
    head = snake['head']
    food = state['food']
    if food.distance(head) < DEFAULT_SIZE: #caso a distância entre a turtle food e a cabeça seja menos que 15 pixeis
        state['food'].hideturtle() #esconde a comida atual
        create_food(state)#gera outra numa posição aleatória
        add_body(state)#adiciona uma turtle de corpo
        state['score'] += 10#aumenta o score
        check_high_score(state)#vê se o novo score é maior que o high_score

def boundaries_collision(state):

    #função que verifica se existe ou não colisão com os limites do ambiente

    snake = state['snake']
    head = snake['head']
    #como a função .pos() devolve um tuplo, o primeiro índice corresponde ao x, e o segundo a y
    x = head.pos()[0]
    y = head.pos()[1]
    #vejamos um ambiente como um referencial onde a origem é o meio
    if x > MAX_X/2 - DEFAULT_SIZE or x < -MAX_X/2 + DEFAULT_SIZE: #o x max é metade do comprimento total do ambiente, ou seja, metade para o lado positivo e outra metade negativa
        return True # a função devolve True
    if y > MAX_Y/2 - DEFAULT_SIZE or y < -MAX_Y/2 + DEFAULT_SIZE:#o y max é metade do comprimento total do ambiente, ou seja, metade para o lado positivo e outra metade negativa

        return True

    return False    #caso não haja colisão a função devolve False

def check_collisions(state):

    #verifica colisões com o próprio corpo

    body = state['snake']['body']
    snake = state['snake']
    for i in range(len(body) - 1, 1, -1):#percorre a lista que é o valor da key 'body'
        if snake['head'].distance(body[i]) < DEFAULT_SIZE: #caso a distância entre a cabeça e qualquer parte do corpo seja inferior a 15 unidades
            snake['current_direction'] = 'stop' #a posição é mudada para stop
            body.clear() #a lista é limpa
            state['score'] = 0 #score é resetado
            return True     #devolve True
    return boundaries_collision(state)

def hs_congrats(state):
    state['score_board'].clear()
    state['score_board'].write("NEW HIGH SCORE: {} ".format(state['high_score']), align="center",
                               font=("Helvetica", 24, "normal"))

def derrota(state):

    #função ativada quando o jogador perde

    print("YOU LOSE!")  #print da mensagem de derrota
    init_map('red')
    update_score_board(state)
    turtle.write("YOU LOSE", move=False, align='center', font=('Arial', 30, 'normal')) #escreve no ecrâ 'YOU LOSE' no formato indicado
    if(state['new_high_score'] == True): #caso o score feito for maior que o high_score
        hs_congrats(state)
        write_high_score_to_file(state) #ativa a função de escrita no ficheiro

def main():
    try:
        # Debug output before the loop starts
        print("Starting main loop")
        init_map('light green')
        state = init_state()
        setup(state)
        while not check_collisions(state):
            # Debug output inside the loop
            print("Running main loop")
            state['window'].update()
            check_if_food_to_eat(state)
            move_body(state)
            move(state)
            update_score_board(state)
            time.sleep(SPEED)
        derrota(state)
        time.sleep(2)  # tempo da mensagem de derrota
    except Exception as e:
        # If an exception occurs, print it out
        print(f"An error occurred: {e}")
    finally:
        # Ensure the window stays open until a click
        print("Click to exit.")
        turtle.exitonclick()

main()


