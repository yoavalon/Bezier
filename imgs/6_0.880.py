d = DslBezier()

d.position_pen(2,2)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
