d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.position_pen(3,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)

d.end()
