d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(3,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
