d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.N, Length.short)
d.position_pen(1,2)

d.end()
