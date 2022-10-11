d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)

d.end()
