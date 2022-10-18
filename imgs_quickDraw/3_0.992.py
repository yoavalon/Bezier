d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(2,1)
d.position_pen(3,0)

d.end()
