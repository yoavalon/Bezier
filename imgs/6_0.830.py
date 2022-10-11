d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
