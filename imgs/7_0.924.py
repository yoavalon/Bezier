d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)

d.end()
