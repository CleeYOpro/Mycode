# This code 'looks right', but it contains an error: the gold rectangle is too
# large! The autograder will not accept it until the gold rectangle is not
# overlapped by the blue and red rectangles.
### (HINT: Try checking your code! What does it tell you is wrong?)
### Fix Your Code Here ###
Rect(50, 100, 300, 100, fill='gold')

# This correctly draws the blue and red rectangles.
Rect(50, 200, 300, 50, fill='navy')
Rect(50, 250, 300, 50, fill='crimson')
