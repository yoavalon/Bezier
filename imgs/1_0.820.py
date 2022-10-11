d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(1,3)

d.end()
