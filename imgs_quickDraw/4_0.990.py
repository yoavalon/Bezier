d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.position_pen(0,0)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)

d.end()
