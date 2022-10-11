d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.short)

d.end()
