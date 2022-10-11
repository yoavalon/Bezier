d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)

d.end()
