d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
