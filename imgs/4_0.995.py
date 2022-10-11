d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.E, Length.medium)

d.end()
