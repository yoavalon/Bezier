d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)

d.end()
