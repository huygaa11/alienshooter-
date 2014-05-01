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

	def _init_(self):
		placeContainer()
		##buildGrid()
		placeCannon()
		"""#loadBubble()
		#showGameScore()
		stage.addEventListener(KeyboardEvent.KEY_DOWN, onKDown);
		stage.addEventListener(KeyboardEvent.KEY_UP, onKUp);
		addEventListener(Event.ENTER_FRAME, onEFrame);"""
		
	#Function to place cannon at the bottom of screen and halfway across the screen 
	def placeCannon(self): 
		print "placeCannon"
		"""cannon=new cannon_mc()
		addChild(cannon)
		cannon.y=450
		cannon.x=R*8"""
     	
	#Function that handles when the user presses one of the arrow keys on the keyboard
	#onKDown(e:KeyboardEvent): 
	def onKDown(self):
		print "onKDown"
		"""check the doc for pygame.key
     	switch(e.keyCode)
			#user hits the left arrow, cannon spins left 
       		case 37:
         		left=True
        		break
			#user hits the right arrow, cannon spins right 	 
       		case 39:
         		right=True
        		break
			#user hits up arrow, fires bubble 	 
			case 38:
				if fire==False: 
					fire=True
           			radians=(self.cannon.rotation-90)*self.DEG_TO_RAD
           			self.vx=self.BUBBLE_SPEED*math.cos(radians)
           			self.vy=self.BUBBLE_SPEED*math.sin(radians)
				    break"""
					
	#Function that handles when the user is not pressing on on the keyboard 
	#onKUp(e:KeyboardEvent):
	def onKUp(self):
		print "onKUp"
		"""switch(e.keyCode) 
     		case 37:
         		left=False
        		break
       		case 39:
         		right=False
        		break"""	
        		
    #onEFrame(e:Event): 
	def onEFrame(self):
		print "onEFrame"
		"""#user hits the left arrow and rotates the cannon to the left 
     	if self.left==True and self.cannon.rotation >= -70:
       		self.cannon.rotation-=self.ROT_SPEED
    		
		#rotate the cannon to the right when the user hits the right arrow 
    	if self.right==True and self.cannon.rotation <= 70 
       		self.cannon.rotation+=self.ROT_SPEED 
				
		#code to handle once bubble has been fired 
		#handles bub
		if self.fire==True: 
				self.bubble.x+=self.vx
				self.bubble.y+=self.vy
				
				#when bubble bounces off the wall respond accordingly 
				if bubble.x<self.R: 
					self.bubble.x=R
					slef.vx*=-1
       			if bubble.x>self.R*15:
         			self.bubble.x=self.R*15
         			self.vx*=-1
				#if bubble hits the top of the screen, locks in
       			if self.bubble.y<R:
					parkBubble()
				
				#check all bubbles in grid to see if bubble that has been fired has collided with them 
				else:
					for i in self.bubCont.numChildren:
						#tmp:self.bubble_mc
						tmp = i #as bubble_mc;
						if collide(tmp):
							parkBubble()
							break"""
		
	#Function to build grid and background
	def placeContainer(self): 
		print "placeContainer"
		"""self.bubCont=new Sprite()
		self.borderLine= new Sprite()
     	addChild(bubCont);
		addChild(borderLine);
     	bubCont.graphics.lineStyle(1,0xffffff,0.2);
		#Draws borderline to indicate where right edge of the field is
		borderLine.graphics.lineStyle(10,0xffffff,0.2);
		borderLine.graphics.moveTo(16*R+8,0);
		borderLine.graphics.lineTo(16*R+8, 480);
		self.gridBuilding = True
     	for i in self.numRows:
			#fieldArray[i] = new Array();
       		for j in self.evenCols:
				#if it's an even row start grid at the left side of the screen 
				if i%2==0:
         			#bubCont.graphics.drawCircle(R+j*R*2,R+i*D,R);
					self.fieldArray[i][j]=0;
					#Load the first 7 rows with bubbles
					if i<8:
						bubble = new bubble_mc();
						addChild(bubble);
						bubble.gotoAndStop(math.floor(math.random()*5))+1
						bubble.x = self.R+j*self.R*2
						bubble.y = self.R+i*self.D
						parkBubble()
					else:
						#if it's an odd row start grid slightly offset of left side of screen
						#odd rows contain one less column than even rows 
						if j<self.oddCols: 
							#bubCont.graphics.drawCircle(2*R+j*R*2,R+i*D,R);
							self.fieldArray[i][j]=0;
							#Build the first 7 rows with bubbles 
							if i<8:
								bubble = new bubble_mc();
								addChild(bubble);
								bubble.gotoAndStop(math.floor(math.random()*5))+1
								bubble.x = self.R+j*self.R*2
								bubble.y = self.R+i*self.D
								parkBubble()
		gridBuilding = False
		loadBubble()"""
		
	#Function to load a new bubble into the cannon 
	def loadBubble(self): 
		print "loadBubble"
		"""checkForGameOver()
		bubble = new bubble_mc()
		addChild(bubble)
		bubble.gotoAndStop(math.floor(math.random()*5))+1
		bubble.x=self.R*8
		bubble.y=450"""
 		
 	#Function that checks if the game has been completed and brings up an image indicating whether the user won or lost 
	def checkForGameOver(self):
		print "checkForGameOver"
		"""gameOver = True; 
		for j in evenCols:
			#if bubble all the bubbles have been cleared or if a bubble is in the same line as the cannon end the game
			if fieldArray[0][j] != 0 and j != evenCols-1 and fieldArray[13][j] == 0:
				self.gameOver = False
			elif j != evenCols-1 and fieldArray[13][j] != 0:
				self.gameOver = True
				self.gameLost = True
				self.fire = False
				self.ROT_SPEED = 0
				self.BUBBLE_SPEED = 0
				trace("Game Over")
				break
		if self.gameOver==True:
			self.gameOverField.width = 405
			self.gameOverField.height = 350 
        	self.gameOverField.multiline = True 
        	self.gameOverField.wordWrap = True 
        	#gameOverField.border = True 
        	
        	addChild(gameOverField)
			if self.gameLost==True:
            	self.gameOverField.htmlText = self.gameOverLose
			else:
				self.gameOverField.htmlText = self.gameOverWin
			self.fire = False
			self.ROT_SPEED = 0
			self.BUBBLE_SPEED = 0
			trace("Game Over")"""
			
	#Function to lock bubble in the grid
	def parkBubble(self):
		print "parkBubble"
		"""row=math.floor(bubble.y/self.D)
		col=0
			
		#depending on the row changes the way the column is calculated
		if row%2==0:
			col = math.floor(bubble.x/(self.R*2))
		else:
			col = math.floor((bubble.x-self.R)/(self.R*2))
		
		placed_bubble = new bubble_mc()
		self.bubCont.addChild(placed_bubble)
			
		#place bubbles in correct column depending on the row 
		if row%2==0:
			placed_bubble.x=(col*self.R*2)+self.R
		else:
			placed_bubble.x=(col*self.R*2)+2*self.R
				
		placed_bubble.y=(row*self.D)+self.R
		placed_bubble.gotoAndStop(bubble.currentFrame)
		placed_bubble.name=row+","+col
		self.fieldArray[row][col]=bubble.currentFrame 
		#chainArray=new Array();
		getChain(row,col)
			
		#if 3 bubbles of the same color are connected, remove those bubbles and any corresponding
		if len(self.chainArray)>2 and self.gridBuilding == False:
			for i in self.chainArray:
				self.gameScore = self.gameScore + self.pointsForConnection
				showGameScore()
				#not sure about this so I left this alone
				#with (bubCont)
				#{
				#	removeChild(getChildByName(chainArray[i]));
				#}
				coords = self.chainArray[i].split(",");
				fieldArray[coords[0]][coords[1]]=0;
				}
			removeNotConnected()
		
		#trace("chain: "+chainArray);
		#trace("chain array length is: " + chainArray.length);
			
		removeChild(bubble)
		self.fire=False;
		if self.gridBuilding == False:
			loadBubble()"""
			
	#Function to show the game score on the right side of the screen 
	def showGameScore(self): 
		print "showGameScore"
		"""self.gameScoreField.width = 245
		#gameScoreField.length = 200; 
		self.gameScoreField.background = True 
		self.gameScoreField.backgroundColor = 0x00ffff
		addChild(gameScoreField)
		self.gameScoreField.x = 300
		self.gameScoreField.text = "Score: "+ str(self.gameScore)"""
		
	#Function that determines if two bubbles have collided
	#collide (bub:bubble_mc):Boolean
	def collide(self):
		print "collide"
		"""dist_x=bub.x-bubble.x
		dist_y=bub.y-bubble.y
		trace(math.sqrt(dist_x*dist_x+dist_y*dist_y))
		return math.sqrt(dist_x*dist_x+dist_y*dist_y)<=2*self.R#-4;"""
	
	#Function passed a row and column will check and see if its valid
	#getValue (row:int, col:int)
	def getValue(self, row, col):
		print "getValue"
		"""if self.fieldArray[row] is None:
			return -1
		if self.fieldArray[row][col] is None:
			return -1
				
		return self.fieldArray[row][col]"""
		
	#Function that checks and see if when a bubble locks in, if it is part of a new chain
	#by checking to make sure it's in a valid row and column and it's color is not currently in the chain array
	#isNewChain(row:int,col:int,val:uint):Boolean
	def isNewChain(self, row, col, val):
		print "isNewChain"
		#return val == getValue(row,col) and self.chainArray.indexOf(row+","+col)==-1
		
	#Function that given a row and column checks surrounding spots and sees if they match the 
	#color of the bubble in the given location
	#getChain(row:int, col:int):
	def getChain(self, row, col):
		print "getChain"
		"""self.chainArray.push(row+","+col)
		odd = row%2
		match = self.fieldArray[row][col]
		i = -1
		j=-1
		while i<=1:
			while j<=1:
				if i!=0 or j !=0:
					if i==0 or j==0 or (j==-1 and odd==0) or (j==1 and odd==1): 
             			if isNewChain(row+i,col+j,match): 
               				getChain(row+i,col+j)
            	j+=1
        	i+=1"""
        	
	#Function that tells in a given position in the grid if a bubble exists and if it has any connections 
	#@param(row:int, col:int) return Boolean
	def isNewConnection(self, row, col):
		print "isNewConnection"
		#return getValue(row,col)>0 and self.connArray.indexOf(row+","+col) == -1
		
	#Function that given a position checks for connections at that position and surrounding positions
	#getConnections(row:int,col:int):void
	def getConnections(self, row, col):
		print "getConnections"
		"""self.connArray.push(row+","+col)
		odd=row%2
		i = -1
		j=-1
		while i<=1:
			while j<=1:
				if i!=0 or j !=0:
					if i==0 or j==0 or (j==-1 and odd==0) or (j==1 and odd==1): 
             			if isNewConnection(row+i,col+j): 
               				if row+i==0:
								self.connArray[0] = "connected"
							else:
								self.getConnections(row+i,col+j)
            	j+=1
        	i+=1"""
        	
    #A function used to discover when a bubble is no longer connected to the grid and removes it from the field
	def removeNotConnected(self):
		print "removeNotConnected"
		"""for i in range(13):
			for j in range(8):
				if getValue(i,j)>0:
					#connArray=new Array();
					getConnections(i,j)
					if self.connArray[0] != "connected":
						#not sure about this so I left this alone
						#with (bubCont) 
						#{
						#	removeChild(getChildByName(i+","+j));
						#}
						self.fieldArray[i][j]=0"""