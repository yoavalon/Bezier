d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
