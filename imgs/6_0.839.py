d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
