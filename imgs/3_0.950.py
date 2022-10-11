d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)

d.end()
