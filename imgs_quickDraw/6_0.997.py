d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)

d.end()
