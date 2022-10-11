d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NW, Length.short)
d.position_pen(0,3)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
