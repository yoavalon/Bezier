d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.long)

d.end()
