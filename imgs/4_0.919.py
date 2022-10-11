d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
