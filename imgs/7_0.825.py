d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
