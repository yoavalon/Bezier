d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.long)

d.end()
