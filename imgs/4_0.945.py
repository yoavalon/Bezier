d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
