d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)

d.end()
