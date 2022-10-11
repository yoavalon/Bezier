d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.SW, Length.medium)

d.end()
