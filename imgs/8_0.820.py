d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)

d.end()
