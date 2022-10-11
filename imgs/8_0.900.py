d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.short)

d.end()
