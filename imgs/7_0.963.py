d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)

d.end()
