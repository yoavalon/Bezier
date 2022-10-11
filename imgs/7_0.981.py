d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,0)

d.end()
