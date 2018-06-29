# simple_robotics_vision
## the introduction of this tournament.
#### the track of the game show in the picutue behind
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/track1.jpg)
#### we need sorting the circle one from a pile of things and pick it up and put it in another side
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/sortting.jpg)
#### our robot prototype
#### using one singal camera logitech C310,slave computer is STM32 F429 ,host computer is raspberry 3B
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/robotprototype.jpg)
### about my code in robotics vision,the code can work well on raspberry 3B, written in `python 3`
#### when detect circle stop and adujust the vision of the car until degree of the edge of trace becomes 0 ,according to the degree feedback,the 13 number means 3bits-x,3bits-y,3bits-degree,3bites-distant,1bite-turnright signal
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/result2.png)
#### then move to a setting distance from edge , according to the distant and circle coordinate of vision feedback
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/result1.png)
#### then pick up the circle,and put it to another side
#### if there is no circle in the vision,the robot walk forward,according to the degree and distant
#### if found the rightturn signal ,robot will turn right
![](https://github.com/JanusTan/Auto_Sorting_MovingRobotCVModule/blob/master/result0.png)
