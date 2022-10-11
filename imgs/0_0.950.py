d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.long)
d.position_pen(3,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
