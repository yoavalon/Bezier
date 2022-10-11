d = DslBezier()

d.position_pen(1,0)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)

d.end()
