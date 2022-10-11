d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)

d.end()
