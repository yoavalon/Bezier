d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.position_pen(3,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,1)

d.end()
