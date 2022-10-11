d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
