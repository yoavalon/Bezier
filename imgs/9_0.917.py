d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SE, Length.medium)

d.end()
