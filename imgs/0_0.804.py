d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
