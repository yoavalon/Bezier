d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,2)

d.end()
