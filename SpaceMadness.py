#Importing the random class.
import random

#Setting the background color
#Disabling all walls so that we can move through them
stage.set_background("scrollingspace")
stage.disable_all_walls()

#Creating the actual dimensions of space.

#Generating the inital text on the screen.
speed_text = codesters.Text("Press Up To Speed Up", 0, 0, "black")
score_text = codesters.Text("Score: 0", 150, 220, "black")

#Generating the rocket and its position.
player = codesters.Sprite("rocket", 0, -200)
player.set_size(.5)

#Creating empty arrays for the asteriod and obstacles
asteriods = []
obstacles = []

#Inital values for score and speed.
score = 0
speed = -5

#Boolean variable which checks the game state of the program.
game_over = False

#Creating the scenery for the game.
def create_scenery():
    #Generates 10 asteriods
    for row in range(8):
        #Computer selects a number between 1 and 7.
        asteriod_num = random.randint(1, 7)
        #Generates obstacles on the left or right side.
        side = random.choice([-1, 1])
        
        #Creating the asteriod object.
        asteriod = codesters.Sprite("asteroid".format(asteriod_num), 230*side, 250-row*50)
        asteriod.set_size(.7)
        
        #once you create the asteriod object, add that object to the list.
        asteriods.append(asteriod)
        
    #Iterates though the populated list
    #For every asteriod object, you want to set the speed properly.
    for asteriod in asteriods:
        asteriod.set_y_speed(speed)

create_scenery()

#Creates the speeding up class so the rocket can speed up.
def speed_up():
    
    global speed
    #If the speed is greater than -15, the rocket will speed up.
    if speed > -15:
        speed -= 1
    #Hides text when user speeds up
    if speed < -8:
        speed_text.hide()
stage.event_key("up", speed_up)

#Creates braking class so rocket can slow down.
def brake():
    
    global speed
    #If the speed is less than -4, the rocket will slow down.
    if speed < -4:
        speed += 1
    #Makes text appear when user slows down.
    if speed >= -8:
        speed_text.show()
stage.event_key("down", brake)

#Creates moving left class so the rocket can move left.
def left():
    player.move_left(20)
stage.event_key("left", left)

#Creates moving right class so the rocket can move right.
def right():
    player.move_right(20)
stage.event_key("right", right)

#
def create_obstacle():
    #
    image = random.choice(["meteor1", "ufo"])
    #
    sprite = codesters.Sprite(image, random.randint(-180,180), 350)
    sprite.set_size(.5)
    
    #If computer selects rocket, it rotates it 180 and it goes 5 times your speed.
    
    if image == "meteor1":
        sprite.set_rotation(-90)
        sprite.set_y_speed(-5+speed)
    
    elif image == "ufo":
        sprite.set_size(.7)
    
    else:
        sprite.set_y_speed(speed)
    
    obstacles.append(sprite)
    
#Creating class for collisions
def collision(player, hit_sprite):
    
    #Importing our global variables.
    global speed, game_over
    
    #If the rocket hits an obstacle or asteriods, the game ends
    if hit_sprite in obstacles or hit_sprite in asteriods:
        
        speed = 0
        game_over = True #Change the game state.
        speed_text.show()
        speed_text.set_text("Game Over!")
        
        #Creates the animation of the rocket spinning our.
        player.set_y_speed(-5)
        player.turn_left(1000) # <-- Revolutions of rocket.
player.event_collision(collision)

#Creates class for our score during the game.
def update():
    
    global score, speed
    #Score is equal to the abolute value of the users speed + 7.
    if speed < -8:
        score += abs(speed+7)
        score_text.set_text("Score: {}".format(score))
    
    #asteriod speed is equal to the rocket speed.
    for asteriod in asteriods:
        asteriod.set_y_speed(speed)
        
        #Nested if condition
        if asteriod.get_y() < -300: # <-- If condition checking.
            asteriod.set_y(300) #<-- asteriods respawn at the top.
    
    #Setting speed for obtacles.
    for obs in obstacles:
        #Speed for Meteor.
        if obs.get_image_name() == "meteor1":
            obs.set_y_speed(-5+speed)
        else:# <-- UFO Speed.
            obs.set_y_speed(speed)
        
        #Once it hits the bottom of the screen then it removes the obstacles.
        if obs.get_y() < -300:
            obstacles.remove(obs)
stage.event_interval(update, .1)
    
def main():
    
    #While loop checking the game state. While is not = to True.
    #If the game fuction is not over, run the fucnction to create the obstacles.
    
    while not game_over:
        create_obstacle()
        stage.wait(random.uniform(.1, 1.5))
main()



