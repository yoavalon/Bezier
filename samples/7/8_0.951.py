d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.position_pen(2,2)
d.position_pen(0,2)
d.position_pen(2,2)

d.end()
