d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)

d.end()
