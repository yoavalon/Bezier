d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.position_pen(1,2)
d.position_pen(1,1)

d.end()
