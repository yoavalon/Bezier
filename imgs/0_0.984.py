d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
