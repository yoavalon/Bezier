d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
