d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(3,1)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
