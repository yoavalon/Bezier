d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)

d.end()
