d = DslBezier()

d.position_pen(2,2)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)

d.end()
