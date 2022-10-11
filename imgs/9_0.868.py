d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)

d.end()
