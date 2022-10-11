d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(0,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.short)

d.end()
