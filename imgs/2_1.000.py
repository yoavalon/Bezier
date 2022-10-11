d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
