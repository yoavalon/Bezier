d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,3)

d.end()
