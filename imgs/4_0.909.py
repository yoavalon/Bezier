d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)

d.end()
