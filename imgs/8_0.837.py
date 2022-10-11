d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,2)

d.end()
