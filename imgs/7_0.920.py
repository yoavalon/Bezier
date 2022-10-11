d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NW, Length.short)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,0)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)

d.end()
