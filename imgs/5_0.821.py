d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)

d.end()
