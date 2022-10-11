d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)

d.end()
