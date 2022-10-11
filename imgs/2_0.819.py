d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
