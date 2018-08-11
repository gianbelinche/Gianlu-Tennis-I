import pygame
from random import randint

def score_setter():
	"""Returns a dictionary with the score images as values, and strings as keys, in the form: score1-score2"""
	scores = {}
	for x in [0,15,30,40]:
		for y in [0,15,30,40]:
			sc = "{}-{}".format(x,y)
			score = pygame.image.load(sc+".png")
			score = pygame.transform.rotozoom(score,0,0.3)
			scores[sc] = score
	score1 = pygame.image.load("40-Ad.png")
	score1 = pygame.transform.rotozoom(score1,0,0.3)
	scores["40-Ad"] = score1
	score2 = pygame.image.load("Ad-40.png")
	score2 = pygame.transform.rotozoom(score2,0,0.3)
	scores["Ad-40"] = score2	
	return scores		


def Initializer():
	"""initialize the pygame module"""
	pygame.init()
	# load and set the logo
	logo = pygame.image.load("logo.jpg")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Gianlu Tennis I")
	screen_width = 800
	screen_height = 462
	screen = pygame.display.set_mode((screen_width,screen_height))
	return screen,screen_height,screen_width
	

def player_movement(xpos,ypos,screen_height,screen_width,step_x_press,step_y_press,screen,bgd_image,image,oponent,ball,xposop,yposop,xposball,yposball,score):
	"""Moves the player"""
	pressedkeys = pygame.key.get_pressed()
	if pressedkeys[pygame.K_RIGHT] or pressedkeys[pygame.K_d]:
		if xpos>screen_width-70:
			step_x_press = -step_x_press
		screen.blit(bgd_image, (0,0))
		xpos += step_x_press
		if step_x_press < 0:
			step_x_press = -step_x_press
		# now blit the smily on screen
		screen.blit(ball, (xposball,yposball))
		screen.blit(oponent,(xposop,yposop))
		screen.blit(image, (xpos, ypos))
		screen.blit(score,(0,340))
		# and update the screen (dont forget that!)
		pygame.display.flip()	
	if pressedkeys[pygame.K_LEFT] or pressedkeys[pygame.K_a]:
		if xpos<0:
			step_x_press = -step_x_press
		screen.blit(bgd_image, (0,0))
		xpos -= step_x_press
		if step_x_press < 0:
			step_x_press = -step_x_press		
		# now blit the smily on screen
		screen.blit(ball, (xposball,yposball))
		screen.blit(oponent,(xposop,yposop))
		screen.blit(image, (xpos, ypos))
		screen.blit(score,(0,340))
		# and update the screen (dont forget that!)
		pygame.display.flip()	
	if pressedkeys[pygame.K_DOWN] or pressedkeys[pygame.K_s]:
		if ypos>screen_height-176:
			step_y_press = -step_y_press
		screen.blit(bgd_image, (0,0))
		ypos += step_y_press
		if step_y_press < 0:
			step_y_press = -step_y_press
		# now blit the smily on screen
		screen.blit(ball, (xposball,yposball))
		screen.blit(oponent,(xposop,yposop))
		screen.blit(image, (xpos, ypos))
		screen.blit(score,(0,340))
		# and update the screen (dont forget that!)	
		pygame.display.flip()
	if pressedkeys[pygame.K_UP] or pressedkeys[pygame.K_w]:
		if ypos<50:
			step_y_press = -step_y_press
		screen.blit(bgd_image, (0,0))
		ypos -= step_y_press
		if step_y_press < 0:
			step_y_press = -step_y_press
		# now blit the smily on screen
		screen.blit(ball, (xposball,yposball))
		screen.blit(oponent,(xposop,yposop))
		screen.blit(image, (xpos, ypos))
		screen.blit(score,(0,340))
		# and update the screen (dont forget that!)	
		pygame.display.flip()
	return xpos,ypos,step_x_press,step_y_press	

def ball_movement(initial,final):
	"""Giving the initial and final positions, it returns the velocitys of the ball"""
	xinitial, yinitial = initial
	xfinal, yfinal = final
	xtravel = xfinal - xinitial
	ytravel = yfinal - yinitial
	yvel = -3
	if yfinal > yinitial:
		yvel*= -1
	xvel = (xtravel/ytravel) * yvel
	return xvel,yvel	

def move_ball(ball,xvel,yvel,xposball,yposball,xpos,ypos,initial,final,bgd_image,oponent,image,screen,xposop,yposop,score):
	"""it moves the ball from one point to the other"""
	#if (initial[0] < final[0] and xposball < final[0]) or (initial[0] > final[0] and xposball > final[0]):
	xposball += xvel
	#if (initial[1] < final[1] and yposball < final[1]) or (initial[1] > final[1] and yposball > final[1]):	
	yposball += yvel
	screen.blit(bgd_image, (0,0))
	screen.blit(oponent,(xposop,yposop))
	screen.blit(image, (xpos, ypos))
	screen.blit(ball,(xposball,yposball))
	screen.blit(score,(0,340))
	pygame.display.flip()
	return xposball,yposball

def oponent_movement(final_op,xposop,yposop,initial_op,oponent,ball,image,screen,xpos,ypos,xposball,yposball,bgd_image,opvel,score):
	"""Defines where the oponent is going to move"""
	oponent_finalx = final_op[0]
	oponent_initialx = initial_op[0]
	if (xposop < oponent_finalx and oponent_finalx > oponent_initialx):
		xposop += opvel
	elif (xposop > oponent_finalx and oponent_finalx < oponent_initialx):
		xposop -= opvel
	screen.blit(bgd_image, (0,0))
	screen.blit(image, (xpos, ypos))
	screen.blit(ball,(xposball,yposball))
	screen.blit(oponent,(xposop,yposop))
	screen.blit(score,(0,340))
	pygame.display.flip()	
	return xposop,yposop	

def oponent_shoot(xposball,xposop,yposball,yposop):
	"""Makes the oponent shoot"""
	initial = (xposball,yposball)
	prob = randint(1,3)
	if prob == 1:
		final = (600,300)
	elif prob == 2:
		final = (150,300)	
	else:
		final = (387,300)	
	xvel, yvel = ball_movement(initial,final)
	final_op = (370,10)
	initial_op = (xposop,yposop)
	return initial,final,xvel,yvel,final_op,initial_op	

def restart(screen,bgd_image,image,ball,oponent,score):
	"""It restarts the point"""
	xposball = 450
	yposball = 200
	xpos = 410
	ypos = 215
	xvel= 0
	yvel= 0
	xposop = 375
	yposop = 10
	final_op = (xposop,yposop)
	screen.blit(bgd_image, (0,0))
	screen.blit(image, (xpos, ypos))
	screen.blit(ball, (xposball,yposball))
	screen.blit(oponent,(xposop,yposop))
	screen.blit(score,(0,340))
	pygame.display.flip()
	return xposop,yposop,xposball,yposball,xpos,ypos,xvel,yvel,final_op

def ball_bounce(yposball,xposball,xvel,yvel):
	"""Makes the ball "bounce" """
	if yposball <= 70:
		if xposball < 280:
			xvel = -1
		elif xposball >280 and xposball < 390:
			xvel = 0
		else:
			xvel = 1		
		yvel = -1
	elif yposball >= 300:
		if xposball < 160:
			xvel = -3
		elif xposball > 160 and xposball < 390:
			xvel = 0
		else:		
			xvel = 3
		yvel = 2
	return xvel,yvel			

def scores_manager(score_player,score_computer,scores,screen,player_won,bgd_image,image,ball,oponent,xpos,ypos,xposball,yposball,xposop,yposop):
	"""Ejecuta un game del partido"""
	if player_won:
		if score_player == 0 or score_player == 15:
			score_player += 15
		elif score_player == 30:
			score_player += 10	
		elif score_player == 40 and (score_computer != "Ad" and score_computer != 40):
			score_player = 0
			score_computer = 0
		elif score_player == 40 and score_computer == 40:
			score_player = "Ad"
		elif score_player == 40 and score_computer == "Ad":
			score_computer = 40
		else:
			score_player = 0
			score_computer = 0	
	else:		
		if score_computer == 0 or score_computer == 15:
			score_computer += 15
		elif score_computer == 30:
			score_computer += 10	
		elif score_computer == 40 and (score_player != "Ad" and score_player != 40):
			score_player = 0
			score_computer = 0	
		elif score_computer == 40 and score_player == 40:
			score_computer = "Ad"
		elif score_computer == 40 and score_player == "Ad":
			score_player = 40
		else:
			score_player = 0
			score_computer = 0	

	score = scores["{}-{}".format(score_player,score_computer)]
	screen.blit(bgd_image, (0,0))
	screen.blit(image, (xpos, ypos))
	screen.blit(ball, (xposball,yposball))
	screen.blit(oponent,(xposop,yposop))
	screen.blit(score,(0,340))
	pygame.display.flip()

	return score_player,score_computer,score



# define a main function
def main():
	
	# create a surface on screen that has the size of 800 x 462
	screen,screen_height,screen_width = Initializer()
	scores = score_setter() 	 


	# define the position of the player
	xpos = 410
	ypos = 215
	# how many pixels we move our player each frame
	step_x_press = 1
	step_y_press = 1

	xposball = 450
	yposball = 200

	xposop = 375
	yposop = 10

	opvel = 2
	xvel = 0
	yvel = 0

	score_player = 0
	score_computer = 0

	initial = (xposball,yposball)
	final = (xposball,yposball)
	initial_op = (xposop,yposop)
	final_op = (400,10)
	
	controls = pygame.image.load("controls.png")
	screen.blit(controls, (0,0))
	pygame.display.flip()

	cont = True
	while cont:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
						cont = False 
			if event.type == pygame.QUIT:
				return
						


	score = pygame.image.load("0-0.png")
	score = pygame.transform.rotozoom(score,0,0.3)
	bgd_image = pygame.image.load("Court.jpg") 
	image = pygame.image.load("Jugador.png")
	image.set_colorkey((0,0,255)) 
	ball = pygame.image.load("Pelota.png")
	ball.set_colorkey((0,0,255))
	ball = pygame.transform.rotozoom(ball,0,0.3)
	oponent = pygame.image.load("op.png")
	oponent.set_colorkey((0,0,255))
	oponent = pygame.transform.rotozoom(oponent,0,0.6)
	screen.blit(bgd_image, (0,0))
	screen.blit(image, (xpos, ypos))
	screen.blit(ball, (xposball,yposball))
	screen.blit(oponent,(xposop,yposop))
	screen.blit(score,(0,340))


	pygame.display.flip()
	
	 
	# define a variable to control the main loop
	running = True
	# main loop
	while running:		
		# event handling, gets all event from the eventqueue
		xpos,ypos,step_x_press,step_y_press = player_movement(xpos,ypos,screen_height,screen_width,step_x_press,step_y_press,screen,bgd_image,image,oponent,ball,xposop,yposop,xposball,yposball,score)
		if initial != final:
			step_y_press = 4
			step_x_press = 4
			xposball,yposball = move_ball(ball,xvel,yvel,xposball,yposball,xpos,ypos,initial,final,bgd_image,oponent,image,screen,xposop,yposop,score)
			xposop,yposop =  oponent_movement(final_op,xposop,yposop,initial_op,oponent,ball,image,screen,xpos,ypos,xposball,yposball,bgd_image,opvel,score)

		if xposball < xposop+70 and xposball > xposop-10 and yposball < yposop+70 and yposball>yposop:
			initial,final,xvel,yvel,final_op,initial_op = oponent_shoot(xposball,xposop,yposball,yposop)

		if yposball < 0:
			xposop,yposop,xposball,yposball,xpos,ypos,xvel,yvel,final_op = restart(screen,bgd_image,image,ball,oponent,score)
			score_player,score_computer,score = scores_manager(score_player,score_computer,scores,screen,True,bgd_image,image,ball,oponent,xpos,ypos,xposball,yposball,xposop,yposop)
		
		if yposball > 462:
			xposop,yposop,xposball,yposball,xpos,ypos,xvel,yvel,final_op = restart(screen,bgd_image,image,ball,oponent,score)
			score_player,score_computer,score = scores_manager(score_player,score_computer,scores,screen,False,bgd_image,image,ball,oponent,xpos,ypos,xposball,yposball,xposop,yposop)

		xvel,yvel = ball_bounce(yposball,xposball,xvel,yvel) 	


		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c and xposball < xpos+90 and xposball > xpos+20 and yposball < ypos+40 and yposball > ypos:
					initial = (xposball,yposball)
					final = (500,70) 
					if initial != final:
						xvel,yvel = ball_movement(initial,final)
						final_op = final
						initial_op = (xposop,yposop)
			
				if event.key == pygame.K_z and xposball < xpos+70 and xposball > xpos+20 and yposball < ypos+40 and yposball > ypos:
					initial = (xposball,yposball)
					final = (275,70) 
					if initial != final:
						xvel,yvel = ball_movement(initial,final)
						final_op = final
						initial_op = (xposop,yposop)
			
				if event.key == pygame.K_x and xposball < xpos+70 and xposball > xpos+20 and yposball < ypos+40 and yposball > ypos:
					initial = (xposball,yposball)
					final = (387,70) 
					if initial != final:
						xvel,yvel = ball_movement(initial,final)
						final_op = final
						initial_op = (xposop,yposop)
								

			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False
	

	 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()