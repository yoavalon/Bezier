d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
