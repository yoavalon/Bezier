d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.long)

d.end()
