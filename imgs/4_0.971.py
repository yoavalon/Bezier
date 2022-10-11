d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)

d.end()
