d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,3)

d.end()
