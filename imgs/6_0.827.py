d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.short)

d.end()
