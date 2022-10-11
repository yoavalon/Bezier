d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)

d.end()
