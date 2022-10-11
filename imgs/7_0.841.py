d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)

d.end()
