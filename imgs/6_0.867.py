d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.S, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,0)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)

d.end()
