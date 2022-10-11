d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
