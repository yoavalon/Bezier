d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.short)

d.end()
