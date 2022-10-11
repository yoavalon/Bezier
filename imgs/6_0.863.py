d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
