d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.short)

d.end()
