d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,0)

d.end()
