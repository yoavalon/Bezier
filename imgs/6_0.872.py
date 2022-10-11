d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,2)

d.end()
