d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(2,0)
d.position_pen(1,2)

d.end()
