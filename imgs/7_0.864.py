d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.short)

d.end()
