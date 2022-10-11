d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)

d.end()
