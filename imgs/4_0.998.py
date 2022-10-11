d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.N, Length.short)

d.end()
