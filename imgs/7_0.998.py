d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.short)

d.end()
