d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.NW, Length.medium)

d.end()
