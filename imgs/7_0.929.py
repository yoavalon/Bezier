d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
