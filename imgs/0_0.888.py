d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.short)

d.end()
