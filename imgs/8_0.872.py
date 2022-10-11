d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)

d.end()
