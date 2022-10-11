d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
