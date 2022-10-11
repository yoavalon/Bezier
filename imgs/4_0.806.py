d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.long)

d.end()
