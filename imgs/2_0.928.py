d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
