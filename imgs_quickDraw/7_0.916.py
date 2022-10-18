d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,3)

d.end()
