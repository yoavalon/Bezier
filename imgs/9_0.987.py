d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)

d.end()
