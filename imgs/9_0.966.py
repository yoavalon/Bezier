d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)

d.end()
