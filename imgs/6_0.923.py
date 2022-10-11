d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.position_pen(1,3)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)

d.end()
