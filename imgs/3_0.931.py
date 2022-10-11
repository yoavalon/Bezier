d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.short)

d.end()
