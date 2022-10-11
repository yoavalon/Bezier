d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)
d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
