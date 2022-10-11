d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)

d.end()
