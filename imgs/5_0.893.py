d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,3)

d.end()
