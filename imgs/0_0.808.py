d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
