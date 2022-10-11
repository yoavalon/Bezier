d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)

d.end()
