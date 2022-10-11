d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(2,2)

d.end()
