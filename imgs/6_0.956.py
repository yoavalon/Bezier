d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
