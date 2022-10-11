d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.position_pen(2,2)
d.position_pen(1,1)

d.end()
