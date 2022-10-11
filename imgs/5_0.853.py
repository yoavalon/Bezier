d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)
d.position_pen(3,1)
d.straight_line(Direction.NE, Length.short)

d.end()
