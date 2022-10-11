d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,2)

d.end()
