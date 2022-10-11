d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
