from turtle import *
color('turquoise', 'light blue')
begin_fill()
while True:
    forward(100)
    left(50)
    if abs(pos()) < 1:
        break
end_fill()
tiltangle(30)
title("So majestic!")
done()
