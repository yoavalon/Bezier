d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)

d.end()
