d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(0,2)
d.position_pen(1,1)
d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)

d.end()
