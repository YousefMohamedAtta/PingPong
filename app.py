import turtle  
#setup window
window = turtle.Screen()
window.title("Ping Pong Game By YousefMohamed")
window.setup (width=800, height=600)
window.tracer(0)#set delay for update drawings الامر ده علشان الصور متقطعش ويشتغلوا كانه فيديو
window.bgcolor(.3,.2,.3)# background color (red , green , blue) بتاخد قيم من صفر لحد 1  لو كلهم 0 يبقي اسود ولو 1 يبقي ابيض
#setup game objects
#ball
ball= turtle.Turtle()
ball.speed(0)#darwing speed وبتاخد قيم من0:10 بس ال0=10 يعني بيبقي اسؤع ما يمكن 
ball.shape("circle")
ball.color("Black")
ball.shapesize(stretch_len=1, stretch_wid=1) #  لو انا محددش حجم الكورة بيحددها تلاقئي (20بكسل *20بكسل) ولو انا حددت بيضرب الرقم االحدده في 20بكسل
ball.penup( )#  كل حاجة برسمها وتتحرك بتعمل خطوط كئن قلم ماشي علي طول وبالامر ده بقوله ارفع الاقلم يعني متسيبش خطوط بعديك (stop drawing lines when moving)
ball.goto(x=0 , y=0) #start posirion 
ball_dx , ball_dy = 1 , 1
ball_speed = 0.3
#center_line 
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=0.1,stretch_wid=25)
center_line.penup()
center_line.goto(0,0)
#player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.shapesize(stretch_len=1,stretch_wid=5)
player1.penup( )
player1.goto(-350,0)
#player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_len=1,stretch_wid=5)
player2.penup( )
player2.goto(350,0)
#score text
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(0,260)
score.write("Player1: 0   Player2: 0", align="center", font=("Courier" , 14 , "normal"))
p1_score  , p2_score = 0 , 0
score.hideturtle() #بيخفي السهم التحت الكلام 
#Players Movemont 
# هعمل شوية دوال برمجية الغرض منها تحريك المضربين لفوق او  تحت
players_speed= 20
def P1_move_up():
     player1.sety(player1.ycor() + players_speed)
def P1_move_down():
     player1.sety(player1.ycor() - players_speed)
def P2_move_up():
     player2.sety(player2.ycor() + players_speed)
def P2_move_down():
     player2.sety(player2.ycor() - players_speed)
#Get users inputs (Key Bidings)
window.listen() #tell the window to expect user inputs 
window.onkeypress(P1_move_up,"w") #ensure the keyboard in "EN" and "small"
window.onkeypress(P1_move_down,"s")
window.onkeypress(P2_move_up,"Up")
window.onkeypress(P2_move_down,"Down")
#Game loop  هنعمل اللوب  ده علشان الشاشة متشغلش وتطفي علي  طول
while True:
     window.update() #وبالكود ده بقوله كل مرة الكود بيتكرر اعملي تحديث للشاشة
     #ball movement
     ball.setx(ball.xcor() + (ball_dx * ball_speed))
     ball.sety(ball.ycor() + (ball_dy * ball_speed))
     #ball & borders collisions
     if(ball.ycor() > 290):# 290=> 300(top border) - 10 ( half ball size)
          ball.sety(290)
          ball_dy *=-1 #invert Y direction
     if(ball.ycor() < -290):
          ball.sety(-290)
          ball_dy *=-1
          #ball & playres collisions
          #collision with player1
     if ball.xcor() < -340 and ball.xcor() > -350  and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60) :
         ball.setx(-340) 
         ball_dx *= -1
      #collision with player2
     if ball.xcor() > 340 and ball.xcor() < 350  and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60) :
         ball.setx(340) 
         ball_dx *= -1
     if (ball.xcor() > 390):
          ball.goto(0,0)
          ball_dx *= -1
          score.clear()
          p1_score += 1
          score.write(f"Player1:{p1_score}  Player2: {p2_score}", align="center", font=("Courier" , 14 , "normal"))
     if (ball.xcor() < -390):
          ball.goto(0,0)
          ball_dx *= -1
          score.clear()
          p2_score += 1
          score.write(f"Player1:{p1_score}  Player2: {p2_score}", align="center", font=("Courier" , 14 , "normal"))
    
         
         
