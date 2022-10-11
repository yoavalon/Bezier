d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
