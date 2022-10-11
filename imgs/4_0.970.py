d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.position_pen(1,1)

d.end()
