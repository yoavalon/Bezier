d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
