d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)

d.end()
