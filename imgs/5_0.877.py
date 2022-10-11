d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,2)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
