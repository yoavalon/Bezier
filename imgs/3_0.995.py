d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)

d.end()
