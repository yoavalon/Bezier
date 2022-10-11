d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
