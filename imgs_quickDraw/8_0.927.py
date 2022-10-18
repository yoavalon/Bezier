d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()
