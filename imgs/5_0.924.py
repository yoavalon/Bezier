d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
