d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.position_pen(1,3)

d.end()
