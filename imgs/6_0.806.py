d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
