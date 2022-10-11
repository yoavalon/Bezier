d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,3)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)

d.end()
