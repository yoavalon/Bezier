d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)

d.end()
