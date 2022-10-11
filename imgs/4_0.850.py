d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.short)

d.end()
