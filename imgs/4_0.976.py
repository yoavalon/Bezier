d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.short)

d.end()
