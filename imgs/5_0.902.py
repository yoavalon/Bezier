d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
