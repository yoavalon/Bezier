d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.long)

d.end()
