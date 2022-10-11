d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,3)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
