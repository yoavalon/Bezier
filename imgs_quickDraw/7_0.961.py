d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SW, Length.long)

d.end()
