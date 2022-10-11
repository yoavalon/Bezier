d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)

d.end()
