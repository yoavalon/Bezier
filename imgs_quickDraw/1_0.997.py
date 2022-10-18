d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)
d.position_pen(1,0)
d.straight_line(Direction.W, Length.medium)

d.end()
