d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,2)

d.end()
