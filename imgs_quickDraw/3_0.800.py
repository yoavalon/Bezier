d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
