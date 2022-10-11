d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.position_pen(0,1)

d.end()
