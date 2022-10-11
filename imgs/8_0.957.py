d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
