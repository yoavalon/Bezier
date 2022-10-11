d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.position_pen(1,1)

d.end()
