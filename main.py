from turtle import Screen
import pandas

from score import Score
from state import State


screen =Screen()
screen.setup(725,491)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)
data = pandas.read_csv('50_states.csv')
country_list = data.to_dict(orient='records')
score = Score()
states= []
for country in country_list:
    new_country = State(name= country['state'], x=country['x'] , y=country['y'])
    states.append(new_country)
print(states)
print(country_list)
game_on =True
user_answers_correct=[]
user_not_guess=[state.state for state in states if not state.state in user_answers_correct]


while game_on:
    screen.update()
    user_answer=screen.textinput(f'got {score.score}/{len(states)}', 'write next state:').title()
    if user_answer =='Exit':
        user_not_guess = [state.state for state in states if not state.state in user_answers_correct]
        user_study = {'States': user_not_guess}

        user_table = pandas.DataFrame(user_study)
        user_table.to_csv('States_to_learn.csv')
        break
    else:
        for state in states:
            if state.state == user_answer:
                user_answers_correct.append(state.state)
                state.show_state()
                score.add_score()

