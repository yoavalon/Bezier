d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
