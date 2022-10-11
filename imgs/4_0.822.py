d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.short)

d.end()
