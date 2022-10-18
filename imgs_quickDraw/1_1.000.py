d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)

d.end()
