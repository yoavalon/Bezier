d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)

d.end()
