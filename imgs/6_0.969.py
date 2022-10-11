d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,2)

d.end()
