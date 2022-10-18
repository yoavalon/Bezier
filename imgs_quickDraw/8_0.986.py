d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,3)
d.position_pen(1,0)

d.end()
