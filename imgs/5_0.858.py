d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)

d.end()
