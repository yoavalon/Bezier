d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
