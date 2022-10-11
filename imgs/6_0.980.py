d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NW, Length.medium)

d.end()
