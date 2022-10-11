d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
