d = DslBezier()

d.position_pen(0,1)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
