d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.short)

d.end()
