d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.short)

d.end()
