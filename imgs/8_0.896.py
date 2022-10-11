d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)

d.end()
