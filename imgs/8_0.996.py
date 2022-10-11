d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.long)

d.end()
