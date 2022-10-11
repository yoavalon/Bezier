d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
