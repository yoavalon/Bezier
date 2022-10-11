d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
