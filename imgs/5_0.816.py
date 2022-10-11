d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)

d.end()
