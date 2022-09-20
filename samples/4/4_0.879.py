d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
