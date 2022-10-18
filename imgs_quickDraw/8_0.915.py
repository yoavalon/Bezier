d = DslBezier()

d.position_pen(3,1)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)

d.end()
