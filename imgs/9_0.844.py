d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)

d.end()
