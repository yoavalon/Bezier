d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,3)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)

d.end()
