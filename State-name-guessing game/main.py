from turtle import *
import pandas
import time 

screen = Screen()
screen.setup(width=600,height=600)
image = "C:/Users/Swati/State-name-guessing game/india_map.gif"
screen.addshape(image)
shape(image)

data = pandas.read_csv("C:/Users/Swati/State-name-guessing game/indian_states_coor.csv")
all_states = data.State.to_list()
guessed_state = []

timer_turtle = Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(150, 260)  
timer_turtle.color("red")


start_time = time.time()
time_limit = 10 * 60
while len(guessed_state) < 28:
  

  elapsed_time = int(time.time() - start_time)
  remaining_time = int(time_limit - elapsed_time)
  
  if remaining_time <= 0:
    screen.textinput(title="Time's Up!!",prompt="Time is over!!")
    break

  minutes = remaining_time // 60
  seconds = remaining_time % 60
  timer_turtle.clear()
  timer_turtle.write(f"⏳ Time left: {minutes:02d}:{seconds:02d}", align="center", font=("Arial", 16, "bold"))

  answer_state = screen.textinput(title=f"{len(guessed_state)}/28 are guesses",prompt="What is the next state??")

  if answer_state.title() == "Exit":
    break


  if answer_state.title() in all_states:
    guessed_state.append(answer_state)
    t = Turtle()
    t.hideturtle()
    t.penup()
    sel_data = data[data["State"]==answer_state.title()]
    t.goto(sel_data["X"].item(),sel_data["Y"].item())
    t.write(f"*{answer_state.title()}")


screen.exitonclick()