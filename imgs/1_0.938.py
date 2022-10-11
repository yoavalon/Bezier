d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.position_pen(0,2)

d.end()
