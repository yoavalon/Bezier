d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
