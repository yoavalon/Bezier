d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(3,3)
d.position_pen(1,2)

d.end()
