d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)

d.end()
