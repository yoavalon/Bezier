d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,0)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
