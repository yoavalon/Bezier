d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NW, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)

d.end()
