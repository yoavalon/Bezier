d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)

d.end()
