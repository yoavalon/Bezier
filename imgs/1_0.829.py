d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.long)
d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)

d.end()
