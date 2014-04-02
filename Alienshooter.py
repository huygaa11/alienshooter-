import pygame, sys, math
from pygame.locals import*

class Main:
	#Explanation of "magic" numbers 
	ROT_SPEED=2 #rotate speed for the cannon
	R=18 #set radius for the bubbles
	D=R*math.sqrt(3) #distance between center of the bubbles 
	DEG_TO_RAD=0.0174532925 #conversion rate 
	BUBBLE_SPEED=15 #speed the bubble travels
	numRows=14
	numValidRows=13
	evenCols=8 
	oddCols=7

	#Boolean variables 
	left=False
	right=False
	gameOver=False
	gameLost=False 
	fire=False 
	gridBuilding=False

	#Objects used on the game field 
	#bubCont 
	#borderLine
	#bubble_mc #bubble object 
	#cannon #cannon object 

	#Setting up variables to keep score 
	#gameScoreField:TextField = new TextField();
	pointsForConnection=100
	gameScore=0
		
	#Images used to denote the game has been completed
	#private var gameOverLose:String = "<img src = 'gameoverlose.gif'>";
	#private var gameOverWin:String = "<img src = 'winner.jpg'>";
	#private var gameOverField:TextField = new TextField();
		
		
	vx=0 #velocity of the bubble in the X direction
	vy=0 #velocity of the bubble in the Y direction 
		
	#Arrays to hold sets of bubbles
	fieldArray=[] #array to hold bubbles of the entire field 
	chainArray=[] #array to hold chains of bubble of the same color that is connected
	connArray=[] #array to hold which bubble are connected to

	def _init_():
		placeContainer()
		#buildGrid()
		placeCannon()
		#loadBubble()
		#showGameScore()
		#stage.addEventListener(KeyboardEvent.KEY_DOWN, onKDown);
		#stage.addEventListener(KeyboardEvent.KEY_UP, onKUp);
		#addEventListener(Event.ENTER_FRAME, onEFrame);