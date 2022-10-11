d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
