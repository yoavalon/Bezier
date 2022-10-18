d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
