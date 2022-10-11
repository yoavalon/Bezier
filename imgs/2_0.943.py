d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(0,3)

d.end()
