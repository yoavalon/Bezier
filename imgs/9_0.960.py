d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)

d.end()
