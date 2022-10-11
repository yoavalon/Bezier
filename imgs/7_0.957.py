d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(0,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)

d.end()
