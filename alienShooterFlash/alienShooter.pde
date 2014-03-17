PImage bg; //background image 
float bubbleVelX; //velocity of bubbles in horizontal direction
float bubbleVelY; //velocity of bubble in vertical direction
float bubbleX; //x coordinate of given bubble 
float bubbleY; //y coordinate of given bubble 
boolean haveBubble, drawLayer; 
Bubble fired;
public static final int DIAM = 35; //diameter of bubbles 
public static int redBub; //definition of red bubble

public static int blueBub; //definition of blue bubble

public static int greenBub; //definition of green bubble

public static int blackBub; //definition of black bubble

public static int nextColor; //definition of the nextcolor per bubble 

int bubsPerLayer = width/DIAM; //defines how many bubbles can fit in the diameter
int layerNum = 0; 
int bubsFired = 0; 

int s = second(); //time used to increment bubbles 

ArrayList bubbles; //holds all the bubbles currently in the grid 

color c1 = BLUE_MASK;

//Method to initizalize background image and bubble colors 
void setup() 
{
  size(810,483); //the size of the window 
  frameRate(30); //how often the screen refreshes 
 
  bg = loadImage("battlefield2.jpg"); 
  
  bubbles = new ArrayList();
  redBub = color(255,0,0);
  blueBub = color(0,0,255);
  greenBub = color(0,255,0);
  blackBub = 0x000000;
}


//method that is constantly called to draw all images on screen
void draw() 
{  
   background(bg); //loads background image 
  
  translate(width/2, height); //specifies where to place cannon in window 
  
  float canAngle = atan2(mouseY-height, mouseX-width/2); //calculation to have cannon follow mouse 
  
  rotate(canAngle); //initialize cannon to follow mouse 
  
  //color the rectange the same color as the next bubble 
  fill(nextColor);
  rect(-50, 0, 125, 35); //original -12 -5 
  //line(0, a+10, width, a+10); //lines to help guide user where to shoot 
  //line(0, a-10, width, a-10); //lines to help guide user where to shoot 
  
  rotate(-canAngle); 
  //a = (a + 1)%(width+32);
  stroke(226, 204, 0);
  
  //every five seconds draw a new layer 
  if(second()%5 == 0 && drawLayer == true)
  {
    addLayer();
    drawLayer = false;
  }
  else if(second()%5!= 0)
    drawLayer = true; 
  
    
  translate(-width/2,-height);
  
  
  if(haveBubble)
  {
  //When bubble bounces off left or right wall change direction  
  if((fired.x_coord- DIAM/2)< 0 ||(fired.x_coord + DIAM/2)> width)
    bubbleVelX  = -bubbleVelX; 
  fired.x_coord += bubbleVelX ;
  if(fired.y_coord<0)
    haveBubble = false;
  fired.y_coord += bubbleVelY;
  if(haveBubble)
    //ellipse(bubbleX, bubbleY, 10, 10);
    fired.draw();
  }
  
  //Loop to see if fired bubble has hit any bubbles in the grid 
  for(int i = bubbles.size()-1; i >= 0; i--) 
  {
    // draw bubble to screen
    // draw ellipse using b.x_coord, b.y_coord, etc. 
    Bubble b = (Bubble) bubbles.get(i);
    if(fired != null && bubble_collision(b, fired))
    {
      //if bubble hits above 
      if(fired.y_coord < b.y_coord)
      {
         fired.y_coord = b.y_coord - DIAM+1; 
         fired.row = b.row + 1;
      }
      else
      {
        fired.y_coord = b.y_coord + DIAM-1; 
        fired.row = b.row - 1;
      }
      //if bubble hits on the left
      if(fired.x_coord < b.x_coord)
      {
        if(b.row % 2 == 0)
          fired.col = b.col -1; 
        else
          fired.col = b.col;
          
        fired.x_coord = b.x_coord - DIAM/2;
      }
      else 
      {
       fired.x_coord = b.x_coord + DIAM/2;
       //if bubble hits on the right 
       if(b.row % 2 == 0)
          fired.col = b.col; 
        else
          fired.col = b.col+1;
      }
      
      
      println("Fired Column is " + fired.col + " and its row is " + fired.row);
      bubbles.add(fired);
      
      
      fired = null;
      haveBubble = false;
    }
    b.draw();
  }
  
}

//method to randomly choose color of the bubbles for layers
public int colorChooser()
  { 
    int i = int(random(4)); 
    int col = 0;
    switch (i)
    {
      case 0:
       col = redBub;
       break;
      case 1:
       col = blueBub;
       break;
      case 2:
        col = greenBub;
        break; 
      case 3:
        col = blackBub;
        break;
       default:
         println("The value of i is currently " + i); 
    }
        
      
    return col; 
  }
  
  
  
void mousePressed()
{
  //if a bubble is not currently traveling 
  if(!haveBubble)
  {
    
    float y = mouseY-height;
    float x = mouseX- width/2;
    float hypot = sqrt(x * x + y * y); 
    bubbleVelY = (mouseY-height)/hypot* 5.0;
    bubbleVelX = (mouseX-(width/2))/hypot* 5.0;
    bubbleX = width/2 + 14; //so bubble can fire from middle of cannon 
    bubbleY = height;
    //color c1 = 0x000000;
    fired = new Bubble(bubbleX, bubbleY, nextColor);
    haveBubble = true;
    //chooses the next color of the bubble to be fired 
      nextColor = colorChooser();
    bubsFired++;
  }
}


//Method to add a layer of bubbles when called
public void addLayer()
{
  //println("Entered addLayer method");
  if(bubbles != null) 
  {
    for(int i = bubbles.size()-1; i >= 0; i--)
    {
      Bubble b = (Bubble) bubbles.get(i);
      b.y_coord+=DIAM-1;
     
    }
  } 
  //println("Wlidth is currently " +width);
  //println("Bubnum should be " + width/DIAM);
  int bubNum = width/DIAM;
  //println("Bubnum is currently "+bubNum);
  int startPoint = DIAM/2;
  if (layerNum%2 !=0)
  {
    bubNum--;
    startPoint = DIAM;
  }
  int count = 0; 
   for(int i =0 ; i<bubNum ; i++)
   {
     Bubble temp = new Bubble(startPoint, DIAM/2, c1,i, layerNum);
     bubbles.add(temp); 
     count++;
     startPoint+= DIAM; 
   }
   layerNum++;
   //println("Count is " + count);
}

/**
 * Check if two bubbles collide
 * x_1, y_1, radius_1 defines the first circle
 * x_2, y_2, radius_2 defines the second circle */
boolean bubble_collision(Bubble b1, Bubble b2)
{
  return dist(b1.x_coord, b1.y_coord, b2.x_coord, b2.y_coord) < b1.radius + b2.radius;
}


/**
* Bubble class to define bubbles
* defines what properties a bubble holds 
* and actions that a bubble can perform
*/

class Bubble 
{

  float x_coord;
  float y_coord;
  float radius;
  Bubble[] neighbors = new Bubble[6];
  color colorBub;
  int matched_neighbor_count;
  int col;
  int row;
  
  public Bubble(float tempX_coord, float tempY_coord, color tempColorBub) 
  {
    // initialize Bubble here
    x_coord = tempX_coord;
    y_coord = tempY_coord;
    
    //set color of bubble to be the defined color
    colorBub = tempColorBub;
    matched_neighbor_count = 0;
    radius = DIAM/2;
    
  }
  
  public Bubble(float tempX_coord, float tempY_coord, color tempColorBub, int tempCol, int tempRow) 
  {
    // initialize Bubble here
    x_coord = tempX_coord;
    y_coord = tempY_coord;
    colorBub = colorChooser();
    matched_neighbor_count = 0;
    radius = DIAM/2;
    col = tempCol;
    row = tempRow; 
    
  }
  
  public int colorChooser()
  { 
    int i = int(random(4)); 
    int col = 0;
    switch (i)
    {
      case 0:
       col = redBub;
       break;
      case 1:
       col = blueBub;
       break;
      case 2:
        col = greenBub;
        break; 
      case 3:
        col = blackBub;
        break;
       default:
         println("The value of i is currently " + i); 
    }
        
      
    return col; 
  }
  
  public void draw() 
  {
    // this could be called instead of drawing an ellipse in the containing draw method
    // elispe using x_coord, y_coord, etc.
    fill(colorBub);
    ellipse(x_coord, y_coord, DIAM, DIAM);
  }
  
  
  public void addNeighbor(Bubble b, Bubble fixedBub) 
  {
    //if bubble snaps in NW position 
    if (b.x_coord < fixedBub.x_coord && b.y_coord < fixedBub.y_coord) {
        fixedBub.neighbors[0] = b; //add new bubble as fixed bubble NW neighbord 
        b.neighbors[3] = fixedBub; //add fixed bubble as new bubble's SE neighbord 
    }
    //if bubble snaps in NE position 
    else if (b.x_coord > fixedBub.x_coord && b.y_coord < fixedBub.y_coord) {
        fixedBub.neighbors[1] = b; //add new bubble as fixed bubble NE neighbor 
        b.neighbors[4] = fixedBub; //add fixed bubble as new bubb;e's SW neighbor
    } 
    //if bubble snaps in E position     
    else if (b.x_coord > fixedBub.x_coord && b.y_coord == fixedBub.y_coord) { 
        fixedBub.neighbors[2] = b; //add
        b.neighbors[5] = fixedBub; // add fixed bubble as new bubble's W neighbor 
    }
    //if bubble snaps in SE position 
    else if (b.x_coord > fixedBub.x_coord && b.y_coord > fixedBub.y_coord) {
      fixedBub.neighbors[3] = b; //add new bubble as fixed bubble SE neighbor 
      b.neighbors[0] = fixedBub; //add fixed bubble as new bubble's NW neighbor 
    }
    //if bubble snaps in SW position  
    else if (b.x_coord < fixedBub.x_coord && b.y_coord > fixedBub.y_coord) {
      fixedBub.neighbors[4] = b; //add new bubble as fixed bubble's SW neighbor
      b.neighbors[1] = b; //add fixed bubble as new bubble's NE neighbor 
    }
    //if bubble snaps in W position 
    else if(b.x_coord < fixedBub.x_coord && b.y_coord == fixedBub.y_coord) { 
      fixedBub.neighbors[5] = b; //add new bubble as fixed bubble's W neighbor 
      b.neighbors[2] = fixedBub; //add fixed bubble as new bubble's E neighbor 
    }
    //if color matches add them to each others
    //neighbor count and see if it's time to drop
    //some bubbles 
    if (b.colorBub == fixedBub.colorBub) {
      b.matched_neighbor_count++; 
      fixedBub.matched_neighbor_count++; 
      if(b.matched_neighbor_count >=3 )
        pop(b); 
      if(fixedBub.matched_neighbor_count >=3)
        pop(fixedBub); 
    }
  }
  
  public void pop(Bubble b) { 
    //TODO 
    //check and erase all bubbles attached to the given bubble of the same color 
    //see that all bubbles are still attached to grid, if not erase those bubbles as well
  }
    
    
  public int getValue (
  
  /*public void addNeighbor(Bubble b)
  {
     neighbors[neighbors.size()] = b;
    if(b.colorBub == this.colorBub)
       matched_neighbor_count++; 
  }*/

}

