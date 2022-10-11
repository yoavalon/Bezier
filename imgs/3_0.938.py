d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)

d.end()
