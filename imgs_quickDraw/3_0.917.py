d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)

d.end()
