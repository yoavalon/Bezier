d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
