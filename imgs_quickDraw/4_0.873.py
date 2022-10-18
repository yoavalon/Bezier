d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(2,0)
d.position_pen(3,2)
d.position_pen(2,0)

d.end()
