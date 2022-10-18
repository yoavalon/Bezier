d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,0)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
