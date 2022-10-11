d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)

d.end()
