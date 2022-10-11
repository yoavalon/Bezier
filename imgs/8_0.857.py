d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,2)

d.end()
