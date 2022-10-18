d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
