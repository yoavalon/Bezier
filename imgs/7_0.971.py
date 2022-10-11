d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)

d.end()
